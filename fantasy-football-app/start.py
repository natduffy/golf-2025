#!/usr/bin/env python3
"""
Startup script for the Fantasy Football Player Tracker
"""

import os
import sys
import webbrowser
from pathlib import Path

# Add the src directory to the Python path
src_dir = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_dir))

try:
    from app import app
    print("🏈 Fantasy Football Player Tracker")
    print("=" * 40)
    print("Starting server...")
    print("The app will open in your browser automatically.")
    print("Press Ctrl+C to stop the server.")
    print()
    
    # Open browser after a short delay
    def open_browser():
        webbrowser.open('http://localhost:8001')
    
    import threading
    import time
    timer = threading.Timer(2.0, open_browser)
    timer.start()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=8001)
    
except ImportError as e:
    print("Error: Could not import required modules.")
    print("Make sure you have installed the requirements:")
    print("  pip install -r requirements.txt")
    print(f"Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error starting the app: {e}")
    sys.exit(1)
