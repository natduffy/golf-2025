from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime

app = Flask(__name__)

# Load player data from the master list
def load_player_data():
    """Load and parse player data from the master list markdown file"""
    players = []
    
    # Path to the master list file (relative to the parent directory)
    master_list_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                   'fantasy_football_master_list.md')
    
    try:
        with open(master_list_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('*') and not line.startswith('Here\'s'):
                # Parse player data from lines like "1. Saquon Barkley, RB, Phi – 343.5 🚩"
                if '. ' in line and ' – ' in line:
                    parts = line.split('. ', 1)[1]  # Remove ranking
                    if ', ' in parts and ' – ' in parts:
                        name_pos_team, points_flags = parts.rsplit(' – ', 1)
                        name_pos_team_parts = name_pos_team.split(', ')
                        
                        if len(name_pos_team_parts) >= 2:
                            name = name_pos_team_parts[0]
                            position = name_pos_team_parts[1]
                            team = name_pos_team_parts[2] if len(name_pos_team_parts) > 2 else 'N/A'
                            
                            # Extract points and flags
                            points_str = points_flags.split()[0]
                            try:
                                points = float(points_str)
                            except ValueError:
                                points = 0.0
                            
                            # Extract flags
                            risk_flag = '🚩' in points_flags
                            undervalued_flag = '💎' in points_flags
                            
                            players.append({
                                'name': name,
                                'position': position,
                                'team': team,
                                'projected_points': points,
                                'risk_flag': risk_flag,
                                'undervalued_flag': undervalued_flag
                            })
    
    except FileNotFoundError:
        # Fallback: use sample data if file not found
        try:
            from sample_data import get_sample_players
            players = get_sample_players()
            print("Using sample data - markdown file not found")
        except ImportError:
            # Create minimal sample data if sample_data module not available
            players = [
                {'name': 'Saquon Barkley', 'position': 'RB', 'team': 'Phi', 'projected_points': 343.5, 'risk_flag': True, 'undervalued_flag': False},
                {'name': 'Bijan Robinson', 'position': 'RB', 'team': 'Atl', 'projected_points': 343.1, 'risk_flag': False, 'undervalued_flag': False},
                {'name': 'Christian McCaffrey', 'position': 'RB', 'team': 'SF', 'projected_points': 318.5, 'risk_flag': True, 'undervalued_flag': False},
            ]
            print("Using fallback sample data")
    
    # Remove duplicates by player name (keep the first occurrence)
    seen_players = set()
    unique_players = []
    for player in players:
        if player['name'] not in seen_players:
            seen_players.add(player['name'])
            unique_players.append(player)
    players = unique_players

    # Sort by projected points (descending)
    players.sort(key=lambda x: x['projected_points'], reverse=True)
    
    # Add overall ranking
    for i, player in enumerate(players):
        player['rank'] = i + 1
    
    # Add position ranking
    position_ranks = {}
    for player in players:
        pos = player['position']
        if pos not in position_ranks:
            position_ranks[pos] = 1
        player['position_rank'] = position_ranks[pos]
        position_ranks[pos] += 1
    
    print(f"Total players loaded: {len(players)}")
    print("Players by position:")
    pos_counts = {}
    for player in players:
        pos = player['position']
        pos_counts[pos] = pos_counts.get(pos, 0) + 1
    for pos, count in sorted(pos_counts.items()):
        print(f"{pos}: {count} players")
    
    return players

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/players')
def get_players():
    """API endpoint to get all players"""
    players = load_player_data()
    return jsonify(players)

@app.route('/api/players/search')
def search_players():
    """API endpoint to search players"""
    query = request.args.get('q', '').lower()
    position_filter = request.args.get('position', '')
    risk_only = request.args.get('risk_only', 'false').lower() == 'true'
    undervalued_only = request.args.get('undervalued_only', 'false').lower() == 'true'
    
    players = load_player_data()
    
    # Apply filters
    filtered_players = []
    for player in players:
        # Search query filter
        if query and query not in player['name'].lower() and query not in player['team'].lower():
            continue
        
        # Position filter
        if position_filter and player['position'] != position_filter:
            continue
        
        # Risk filter
        if risk_only and not player['risk_flag']:
            continue
        
        # Undervalued filter
        if undervalued_only and not player['undervalued_flag']:
            continue
        
        filtered_players.append(player)
    
    return jsonify(filtered_players)

@app.route('/api/positions')
def get_positions():
    """API endpoint to get unique positions"""
    players = load_player_data()
    positions = list(set(player['position'] for player in players))
    positions.sort()
    return jsonify(positions)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8001))
    app.run(debug=False, host='0.0.0.0', port=port)
