import requests
import json
from datetime import datetime

# Top 40 odds from OCR for British Open Championship
top40_odds_dict = {
    # Top 40 Odds from Image 1 (negative moneyline format)
    'Scottie Scheffler': '-1100', 'Rory McIlroy': '-700', 'Jon Rahm': '-500', 'Bryson DeChambeau': '-250',
    'Shane Lowry': '-220', 'Ludvig Aberg': '-200', 'Robert MacIntyre': '-190', 'Joaquin Niemann': '-150',
    'Russell Henley': '-150', 'Corey Conners': '-140', 'Justin Thomas': '-140', 'Patrick Reed': '-125',
    'Brooks Koepka': '-120', 'Aaron Rai': '-115', 'Hideki Matsuyama': '-115', 'Sam Burns': '-115',
    'J.J. Spaun': '-110', 'Ryan Fox': '-110', 'Harris English': '-105',
    
    # Top 40 Odds from Image 2 (mixed format)
    'Tommy Fleetwood': '-275', 'Collin Morikawa': '-250', 'Xander Schauffele': '-220', 'Tyrrell Hatton': '-200',
    'Viktor Hovland': '-180', 'Matthew Fitzpatrick': '-150', 'Sepp Straka': '-150', 'Justin Rose': '-140',
    'Patrick Cantlay': '-140', 'Adam Scott': '-120', 'Jordan Spieth': '-120', 'Ben Griffin': '-115',
    'Jason Day': '-115', 'Chris Gotterup': '-110', 'Keegan Bradley': '-110', 'Cameron Young': '-105',
    'Harry Hall': '-105', 'Maverick McNealy': '-105', 'Si Woo Kim': '+105', 'Nicolai Hojgaard': '+110',
    'Nick Taylor': '+115', 'Cameron Smith': '+120', 'Tom McKibbin': '+120', 'Bud Cauley': '+130',
    'Max Greyserman': '+130', 'Sungjae Im': '+130', 'Wyndham Clark': '+130', 'Akshay Bhatia': '+140',
    'Carlos Ortiz': '+150', 'Davis Thompson': '+150', 'J.T. Poston': '+150', 'Kevin Yu': '+150',
    'Rasmus Hojgaard': '+150', 'Thomas Detry': '+150', 'Thriston Lawrence': '+150', 'Byeong Hun An': '+160',
    'Brian Harman': '+105', 'Min Woo Lee': '+110', 'Marco Penge': '+115', 'Taylor Pendrith': '+115',
    'Daniel Berger': '+120', 'Tony Finau': '+125', 'Louis Oosthuizen': '+130', 'Rickie Fowler': '+130',
    'Tom Kim': '+130', 'Matt Wallace': '+135', 'Andrew Novak': '+140', 'Christiaan Bezuidenhout': '+150',
    'Dean Burmester': '+150', 'Jordan Smith': '+150', 'Michael Kim': '+150', 'Sergio Garcia': '+150',
    'Thorbjorn Olesen': '+150', 'Aldrich Potgieter': '+160', 'Denny McCarthy': '+160'
}

def fetch_odds():
    API_KEY = "7e28b633936a9e47635d45d4efebcede"
    BASE_URL = "https://api.the-odds-api.com/v4/sports"
    
    try:
        # First, get the sport key for golf British Open Championship
        print("Fetching available sports...")
        sports_response = requests.get(
            f"{BASE_URL}/?apiKey={API_KEY}"
        )
        sports_response.raise_for_status()
        sports_data = sports_response.json()
        
        # Print available sports
        print("\nAvailable sports:")
        for sport in sports_data:
            print(f"- {sport['title']} (key: {sport['key']})")
        
        # Find the golf British Open Championship tournament key
        golf_open_key = None
        for sport in sports_data:
            if "golf_the_open_championship_winner" in sport.get("key", ""):
                golf_open_key = sport["key"]
                break
        
        if not golf_open_key:
            print("Could not find British Open Championship tournament in available sports")
            return None
            
        print(f"\nFound British Open Championship key: {golf_open_key}")
        
        # Get the odds for the tournament
        print("\nFetching tournament odds...")
        odds_response = requests.get(
            f"{BASE_URL}/{golf_open_key}/odds",
            params={
                "apiKey": API_KEY,
                "regions": "us",
                "markets": "h2h,outrights",
                "oddsFormat": "american"
            }
        )
        odds_response.raise_for_status()
        odds_data = odds_response.json()
        
        # Print the structure of the odds data
        print("\nOdds data structure:")
        if odds_data and len(odds_data) > 0:
            event = odds_data[0]
            print(f"\nEvent: {event.get('sport_title')} - {event.get('commence_time')}")
            print("\nAvailable bookmakers:")
            for bookmaker in event.get("bookmakers", []):
                print(f"\n- {bookmaker['title']}")
                for market in bookmaker.get("markets", []):
                    print(f"  - Market: {market['key']}")
                    print(f"    Outcomes: {len(market['outcomes'])}")
                    if market["key"] == "outrights":
                        print("\n    Sample odds:")
                        for outcome in market["outcomes"][:3]:  # Show first 3 odds
                            print(f"    - {outcome['name']}: {outcome['price']}")
        
        # Process odds data
        golfers = []
        if odds_data and len(odds_data) > 0:
            event = odds_data[0]  # Get the first event
            
            # Find DraftKings bookmaker first, then BetMGM as fallback
            draftkings_bookmaker = None
            betmgm_bookmaker = None
            for bookmaker in event.get("bookmakers", []):
                if bookmaker["title"] == "DraftKings":
                    draftkings_bookmaker = bookmaker
                elif bookmaker["title"] == "BetMGM":
                    betmgm_bookmaker = bookmaker
            
            # Use DraftKings if available, otherwise BetMGM, then first available
            selected_bookmaker = draftkings_bookmaker or betmgm_bookmaker
            
            if selected_bookmaker:
                print(f"\nUsing odds from: {selected_bookmaker['title']}")
                for market in selected_bookmaker.get("markets", []):
                    if market["key"] == "outrights":
                        for outcome in market["outcomes"]:
                            name = outcome["name"]
                            odds = outcome["price"]
                            
                            # Check if we already have this golfer
                            if not any(g["name"] == name for g in golfers):
                                # Check if this golfer has Top 40 odds in our dictionary
                                top40_odds = top40_odds_dict.get(name, "N/A")
                                
                                golfers.append({
                                    "name": name,
                                    "win_odds": odds,
                                    "top40_odds": top40_odds,
                                    "make_cut_odds": "N/A"
                                })
            else:
                print("\nDraftKings and BetMGM odds not found, using first available bookmaker")
                if event.get("bookmakers") and len(event["bookmakers"]) > 0:
                    bookmaker = event["bookmakers"][0]
                    print(f"Using odds from: {bookmaker['title']}")
                    for market in bookmaker.get("markets", []):
                        if market["key"] == "outrights":
                            for outcome in market["outcomes"]:
                                name = outcome["name"]
                                odds = outcome["price"]
                                
                                # Check if we already have this golfer
                                if not any(g["name"] == name for g in golfers):
                                    # Check if this golfer has Top 40 odds in our dictionary
                                    top40_odds = top40_odds_dict.get(name, "N/A")
                                    
                                    golfers.append({
                                        "name": name,
                                        "win_odds": odds,
                                        "top40_odds": top40_odds,
                                        "make_cut_odds": "N/A"
                                    })
        
        # Sort golfers by win odds
        golfers.sort(key=lambda x: float(x["win_odds"]) if x["win_odds"] != "N/A" else float('inf'))
        
        # Print remaining API requests
        remaining = odds_response.headers.get('x-requests-remaining', 'unknown')
        print(f"\nRemaining API requests: {remaining}")
        
        return golfers
    
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

def save_odds_to_file(golfers):
    if golfers is not None and len(golfers) > 0:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"british_open_odds_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("2025 British Open Championship Odds\n")
            f.write("=" * 50 + "\n\n")
            f.write("Data sourced from The Odds API (DraftKings/BetMGM)\n")
            f.write("Note: Top 40 and Make Cut odds may not be available\n\n")
            
            for golfer in golfers:
                f.write(f"Golfer: {golfer['name']}\n")
                f.write(f"Win Odds: {golfer['win_odds']}\n")
                f.write(f"Top 40 Odds: {golfer['top40_odds']}\n")
                f.write(f"Make Cut Odds: {golfer['make_cut_odds']}\n")
                f.write("-" * 30 + "\n")
        
        print(f"\nOdds have been saved to {filename}")
        return filename
    else:
        print("No odds data to save")
        return None

def main():
    print("Fetching British Open Championship 2025 odds...")
    golfers = fetch_odds()
    filename = save_odds_to_file(golfers)
    if filename:
        print(f"\nTo view the odds, open {filename}")
        print("To update the web interface, copy this file to the web directory")

if __name__ == "__main__":
    main() 