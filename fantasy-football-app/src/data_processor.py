#!/usr/bin/env python3
"""
Data processor for fantasy football master list
Converts markdown format to structured JSON data
"""

import json
import re
from pathlib import Path

def parse_markdown_file(file_path):
    """
    Parse the fantasy football master list markdown file
    Returns a list of player dictionaries
    """
    players = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Skip empty lines, headers, and notes
            if not line or line.startswith('*') or line.startswith('Here\'s'):
                continue
            
            # Parse player data from format: "1. Saquon Barkley, RB, Phi – 343.5 🚩"
            if '. ' in line and ' – ' in line:
                try:
                    # Extract ranking and player info
                    parts = line.split('. ', 1)
                    if len(parts) != 2:
                        continue
                    
                    ranking = int(parts[0])
                    player_info = parts[1]
                    
                    # Split player info and points/flags
                    if ' – ' not in player_info:
                        continue
                    
                    name_pos_team, points_flags = player_info.rsplit(' – ', 1)
                    name_pos_team_parts = name_pos_team.split(', ')
                    
                    if len(name_pos_team_parts) < 2:
                        continue
                    
                    name = name_pos_team_parts[0]
                    position = name_pos_team_parts[1]
                    team = name_pos_team_parts[2] if len(name_pos_team_parts) > 2 else 'N/A'
                    
                    # Extract projected points
                    points_match = re.search(r'(\d+\.?\d*)', points_flags)
                    if not points_match:
                        continue
                    
                    projected_points = float(points_match.group(1))
                    
                    # Extract flags
                    risk_flag = '🚩' in points_flags
                    undervalued_flag = '💎' in points_flags
                    
                    player = {
                        'rank': ranking,
                        'name': name,
                        'position': position,
                        'team': team,
                        'projected_points': projected_points,
                        'risk_flag': risk_flag,
                        'undervalued_flag': undervalued_flag,
                        'line_number': line_num
                    }
                    
                    players.append(player)
                    
                except (ValueError, IndexError) as e:
                    print(f"Warning: Could not parse line {line_num}: {line}")
                    print(f"Error: {e}")
                    continue
        
        # Sort by projected points (descending)
        players.sort(key=lambda x: x['projected_points'], reverse=True)
        
        # Update rankings after sorting
        for i, player in enumerate(players):
            player['rank'] = i + 1
        
        return players
        
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def save_to_json(players, output_file):
    """Save players data to JSON file"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(players, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved {len(players)} players to {output_file}")
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def print_summary(players):
    """Print a summary of the parsed data"""
    if not players:
        print("No players found!")
        return
    
    print(f"\nParsed {len(players)} players:")
    print(f"Positions: {', '.join(sorted(set(p['position'] for p in players))}")
    print(f"Teams: {', '.join(sorted(set(p['team'] for p in players))}")
    
    high_risk = sum(1 for p in players if p['risk_flag'])
    undervalued = sum(1 for p in players if p['undervalued_flag'])
    
    print(f"High Risk Players: {high_risk}")
    print(f"Undervalued Players: {undervalued}")
    
    avg_points = sum(p['projected_points'] for p in players) / len(players)
    print(f"Average Projected Points: {avg_points:.1f}")
    
    print("\nTop 5 Players:")
    for i, player in enumerate(players[:5]):
        flags = []
        if player['risk_flag']:
            flags.append('🚩')
        if player['undervalued_flag']:
            flags.append('💎')
        flags_str = ' '.join(flags) if flags else ''
        print("{}. {} ({}, {}) - {} {}".format(i+1, player['name'], player['position'], player['team'], player['projected_points'], flags_str))

def main():
    """Main function to process the markdown file"""
    # Path to the master list file (relative to this script)
    script_dir = Path(__file__).parent
    master_list_path = script_dir.parent.parent / 'fantasy-football' / 'fantasy_football_master_list.md'
    
    print("Looking for master list at: {}".format(master_list_path))
    
    if not master_list_path.exists():
        print("Master list file not found at {}".format(master_list_path))
        print("Please ensure the file exists and try again.")
        return
    
    # Parse the markdown file
    players = parse_markdown_file(master_list_path)
    
    if not players:
        print("No players were parsed. Check the file format.")
        return
    
    # Print summary
    print_summary(players)
    
    # Save to JSON
    output_file = script_dir / 'players.json'
    save_to_json(players, output_file)
    
    print(f"\nData processing complete!")
    print(f"JSON file saved to: {output_file}")

if __name__ == '__main__':
    main()
