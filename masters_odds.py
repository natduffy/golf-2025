import requests
import pandas as pd
from datetime import datetime
import json

def scrape_odds():
    # The Odds API configuration
    API_KEY = "7e28b633936a9e47635d45d4efebcede"
    BASE_URL = "https://api.the-odds-api.com/v4/sports"
    
    try:
        # First, get the sport key for golf masters
        print("Fetching available sports...")
        sports_response = requests.get(
            f"{BASE_URL}/?apiKey={API_KEY}"
        )
        sports_response.raise_for_status()
        sports_data = sports_response.json()
        
        # Find the golf masters tournament key
        golf_masters_key = None
        for sport in sports_data:
            if "golf_masters" in sport.get("key", ""):
                golf_masters_key = sport["key"]
                break
        
        if not golf_masters_key:
            print("Could not find golf masters tournament in available sports")
            return None
            
        print(f"Found golf masters key: {golf_masters_key}")
        
        # Get the odds for the tournament
        print("Fetching tournament odds...")
        odds_response = requests.get(
            f"{BASE_URL}/{golf_masters_key}/odds",
            params={
                "apiKey": API_KEY,
                "regions": "us",
                "markets": "h2h,outrights",
                "oddsFormat": "american"
            }
        )
        odds_response.raise_for_status()
        odds_data = odds_response.json()
        
        # Initialize lists to store data
        golfers = []
        win_odds = []
        top20_odds = []
        make_cut_odds = []
        
        # Process odds data
        if odds_data and len(odds_data) > 0:
            event = odds_data[0]  # Get the first event
            
            # Process bookmakers
            for bookmaker in event.get("bookmakers", []):
                for market in bookmaker.get("markets", []):
                    if market["key"] == "outrights":
                        for outcome in market["outcomes"]:
                            name = outcome["name"]
                            odds = outcome["price"]
                            
                            if name not in golfers:
                                golfers.append(name)
                                win_odds.append(odds)
                                top20_odds.append("N/A")  # These markets might not be available
                                make_cut_odds.append("N/A")
        
        # Create DataFrame
        df = pd.DataFrame({
            'Golfer': golfers,
            'Win Odds': win_odds,
            'Top 20 Odds': top20_odds,
            'Make Cut Odds': make_cut_odds
        })
        
        # Print remaining API requests
        remaining = odds_response.headers.get('x-requests-remaining', 'unknown')
        print(f"Remaining API requests: {remaining}")
        
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching odds: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Status code: {e.response.status_code}")
            print("Response content:", e.response.text[:500])
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def save_odds_to_file(df):
    if df is not None and not df.empty:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"masters_odds_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("2025 Masters Tournament Odds\n")
            f.write("=" * 50 + "\n\n")
            f.write("Data sourced from The Odds API\n")
            f.write("Note: Top 20 and Make Cut odds may not be available\n\n")
            
            for _, row in df.iterrows():
                f.write(f"Golfer: {row['Golfer']}\n")
                f.write(f"Win Odds: {row['Win Odds']}\n")
                f.write(f"Top 20 Odds: {row['Top 20 Odds']}\n")
                f.write(f"Make Cut Odds: {row['Make Cut Odds']}\n")
                f.write("-" * 30 + "\n")
        
        print(f"Odds have been saved to {filename}")
    else:
        print("No odds data to save")

def main():
    print("Scraping Masters 2025 odds...")
    odds_df = scrape_odds()
    save_odds_to_file(odds_df)

if __name__ == "__main__":
    main() 