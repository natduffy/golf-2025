# Masters Golf Tournament Odds Scraper

This application scrapes and displays odds for the 2025 Masters Golf Tournament, including:
- Win odds
- Top 20 finish odds
- Make cut odds

## Setup

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with:
```bash
python masters_odds.py
```

The script will:
1. Scrape the latest odds from oddschecker.com
2. Save the results to a text file with timestamp (format: masters_odds_YYYYMMDD_HHMMSS.txt)

## Output Format

The output file will contain:
- Golfer name
- Win odds
- Top 20 finish odds
- Make cut odds

Each golfer's information is separated by a line of dashes for easy reading.

## Note

The odds are scraped from oddschecker.com. Please be aware that:
- The odds are subject to change
- Some odds may not be available for all golfers
- The script requires an internet connection to function 