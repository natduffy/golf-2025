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
        
        # Output just the array of files as expected by the frontend
        print(json.dumps(files))
        
    except Exception as e:
        # Error response
        error_response = {
            'error': str(e)
        }
        
        print('Content-Type: application/json')
        print('Access-Control-Allow-Origin: *')
        print()  # Empty line to separate headers from body
        print(json.dumps(error_response))

if __name__ == '__main__':
    list_odds_files() 