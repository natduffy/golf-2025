import os
import json
import sys

def list_odds_files():
    try:
        # Get all files matching the pattern
        files = [f for f in os.listdir('.') if f.startswith('pga_championship_odds_') and f.endswith('.txt')]
        
        # Sort files by timestamp (newest first)
        files.sort(reverse=True)
        
        # Set headers
        print('Content-Type: application/json')
        print('Access-Control-Allow-Origin: *')
        print()  # Empty line to separate headers from body
        
        # Output JSON
        print(json.dumps(files))
        
    except Exception as e:
        print('Content-Type: application/json')
        print('Access-Control-Allow-Origin: *')
        print()  # Empty line to separate headers from body
        print(json.dumps({"error": str(e)}))

if __name__ == '__main__':
    list_odds_files() 