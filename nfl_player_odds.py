import requests
import json
from datetime import datetime

def fetch_nfl_player_odds():
    API_KEY = "7e28b633936a9e47635d45d4efebcede"
    BASE_URL = "https://api.the-odds-api.com/v4/sports"
    
    try:
        print("Fetching NFL player performance odds...")
        
        # Get NFL sport key
        sports_response = requests.get(
            f"{BASE_URL}/?apiKey={API_KEY}"
        )
        sports_response.raise_for_status()
        sports_data = sports_response.json()
        
        # Find NFL key
        nfl_key = None
        for sport in sports_data:
            if sport.get("key") == "americanfootball_nfl":
                nfl_key = sport["key"]
                break
        
        if not nfl_key:
            print("Could not find NFL in available sports")
            return None
            
        print(f"Found NFL key: {nfl_key}")
        
        # First, let's see what markets are available for NFL
        print("\nChecking available markets for NFL...")
        basic_response = requests.get(
            f"{BASE_URL}/{nfl_key}/odds",
            params={
                "apiKey": API_KEY,
                "regions": "us",
                "oddsFormat": "american"
            }
        )
        basic_response.raise_for_status()
        basic_data = basic_response.json()
        
        if basic_data and len(basic_data) > 0:
            print(f"\nFound {len(basic_data)} NFL events")
            
            # Show the first event to see what markets are available
            first_event = basic_data[0]
            print(f"\nSample Event: {first_event.get('sport_title')} - {first_event.get('commence_time')}")
            print(f"Home: {first_event.get('home_team')}")
            print(f"Away: {first_event.get('away_team')}")
            
            # Show available bookmakers and their markets
            for bookmaker in first_event.get("bookmakers", [])[:3]:  # Show first 3 bookmakers
                print(f"\n  Bookmaker: {bookmaker['title']}")
                for market in bookmaker.get("markets", []):
                    print(f"    Market: {market['key']}")
                    print(f"      Outcomes: {len(market['outcomes'])}")
                    
                    # Show sample outcomes for key markets
                    if market["key"] in ["h2h", "outrights", "spreads", "totals"]:
                        print("      Sample outcomes:")
                        for outcome in market["outcomes"][:3]:  # Show first 3
                            print(f"        - {outcome.get('name', outcome.get('description', 'N/A'))}: {outcome.get('price', 'N/A')}")
        
        # Now let's check for specific player-related markets
        print("\n\nChecking for player-specific markets...")
        
        # Try different market combinations
        market_combinations = [
            "h2h,outrights",  # Basic markets
            "spreads,totals",  # Game lines
            "player_props",    # Player props (if available)
            "futures"          # Season futures (if available)
        ]
        
        for markets in market_combinations:
            try:
                print(f"\nTrying markets: {markets}")
                response = requests.get(
                    f"{BASE_URL}/{nfl_key}/odds",
                    params={
                        "apiKey": API_KEY,
                        "regions": "us",
                        "markets": markets,
                        "oddsFormat": "american"
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                if data and len(data) > 0:
                    print(f"  Success! Found {len(data)} events")
                    event = data[0]
                    print(f"  Sample event: {event.get('home_team')} vs {event.get('away_team')}")
                    
                    # Show what markets we got
                    for bookmaker in event.get("bookmakers", [])[:1]:
                        print(f"    Bookmaker: {bookmaker['title']}")
                        for market in bookmaker.get("markets", []):
                            print(f"      Market: {market['key']} ({len(market['outcomes'])} outcomes)")
                            
                            # Show sample outcomes for interesting markets
                            if market["key"] in ["outrights", "futures"]:
                                print("        Sample outcomes:")
                                for outcome in market["outcomes"][:5]:
                                    print(f"          - {outcome.get('name', outcome.get('description', 'N/A'))}: {outcome.get('price', 'N/A')}")
                else:
                    print(f"  No data returned for markets: {markets}")
                    
            except Exception as e:
                print(f"  Error with markets '{markets}': {e}")
        
        return basic_data
        
    except Exception as e:
        print(f"Error fetching NFL player odds: {e}")
        return None

if __name__ == "__main__":
    print("NFL Player Performance Odds Explorer")
    print("=" * 40)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    odds_data = fetch_nfl_player_odds()
    
    if odds_data:
        print(f"\nSuccessfully fetched data for {len(odds_data)} events")
        print("\nThis data can be used for fantasy football analysis including:")
        print("- Team performance projections")
        print("- Game outcomes and spreads")
        print("- Season-long team futures")
        print("- Player performance context")
    else:
        print("Failed to fetch NFL player odds data")
