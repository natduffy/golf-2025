import os
import json
import sys
import cgi

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
        sys.stdout.write(json.dumps(files))
        sys.stdout.flush()
        
    except Exception as e:
        print('Content-Type: application/json')
        print('Access-Control-Allow-Origin: *')
        print()  # Empty line to separate headers from body
        sys.stdout.write(json.dumps({"error": str(e)}))
        sys.stdout.flush()

if __name__ == '__main__':
    # Check if we're running as a CGI script
    if 'REQUEST_METHOD' in os.environ:
        list_odds_files()
    else:
        # Development mode - just print the files
        files = [f for f in os.listdir('.') if f.startswith('pga_championship_odds_') and f.endswith('.txt')]
        files.sort(reverse=True)
        print(json.dumps(files)) 