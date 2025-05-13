# PGA Championship 2025 Odds Tracker

A web application that displays and tracks betting odds for the 2025 PGA Championship.

## Features

- Displays current betting odds from DraftKings (selected for having the most comprehensive golfer coverage)
- Allows selecting golfers with checkboxes
- Selected golfers are moved to the bottom of the list with a strikethrough effect
- Sortable columns for golfer name, win odds, and top 20 odds
- Reset button to clear all selections
- Smooth animations when selecting/deselecting golfers

## Setup

1. Install Python 3.x
2. Install required packages:
   ```bash
   pip3 install requests
   ```
3. Set up your API key:
   - Get an API key from [The Odds API](https://the-odds-api.com/)
   - Add your API key to `pga_championship_odds.py`

## Usage

1. Fetch the latest odds:
   ```bash
   python3 pga_championship_odds.py
   ```
   This will create a new text file with the current odds.

2. Start the web server:
   ```bash
   python3 server.py
   ```

3. Open your browser to `http://localhost:8000`

## Deployment

### Build Command
```bash
pip3 install -r requirements.txt
```

### Start Command
```bash
python3 server.py
```

The server will start on port 8000. Make sure this port is available in your production environment.

## Files

- `pga_championship_odds.py`: Fetches odds from The Odds API and saves them to a text file
- `list_odds_files.py`: Lists available odds files sorted by timestamp
- `server.py`: Serves the web interface
- `index.html`: Web interface for viewing and interacting with the odds

## Data Source

Odds are sourced from DraftKings via The Odds API. DraftKings was selected as the primary odds provider because it offers:
- The most comprehensive coverage of golfers (155 golfers listed)
- Competitive odds
- Regular updates

## Notes

- The odds are stored in text files with timestamps for historical tracking
- The web interface automatically loads the most recent odds file
- Selected golfers persist until the page is refreshed or the reset button is clicked 