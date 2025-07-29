import requests
import json
from datetime import datetime

# Top 40 odds from OCR (normalized, 'Even' as +100)
top40_odds_dict = {
    'Robert MacIntyre': '+130', 'Tony Finau': '+130', 'Cameron Young': '+140', 'Keegan Bradley': '+140',
    'Andrew Novak': '+160', 'Dean Burmester': '+160', 'Harris English': '+160', 'Matthew Fitzpatrick': '+160',
    'Rickie Fowler': '+160', 'Taylor Pendrith': '+160', 'Mackenzie Hughes': '+170', 'David Puig': '+188',
    'Sahith Theegala': '+188', 'Tom Kim': '+188', 'Jake Knapp': '+190', 'Kurt Kitayama': '+190',
    'Bud Cauley': '+210', 'Lucas Glover': '+210', 'Si Woo Kim': '+130', 'Aaron Rai': '+140',
    'Davis Thompson': '+140', 'Will Zalatoris': '+140', 'Byeong Hun An': '+160', 'Gary Woodland': '+160',
    'J.J. Spaun': '+160', 'Rasmus Hojgaard': '+160', 'Sergio Garcia': '+160', 'Adam Scott': '+170',
    'Stephan Jaeger': '+170', 'Ryan Fox': '+188', 'Thomas Detry': '+188', 'J.T. Poston': '+190',
    'Kevin Yu': '+190', 'Ben Griffin': '+210', 'Jacob Bridgeman': '+210', 'Michael Kim': '+210',
    'Rory McIlroy': '-1000', 'Bryson DeChambeau': '-575', 'Jon Rahm': '-270', 'Collin Morikawa': '-210',
    'Patrick Cantlay': '-175', 'Hideki Matsuyama': '-165', 'Shane Lowry': '-150', 'Viktor Hovland': '-150',
    'Corey Conners': '-125', 'Sepp Straka': '-125', 'Jason Day': '+100', 'Russell Henley': '+100',
    'Min Woo Lee': '+105', 'Cameron Smith': '+125', 'Maverick McNealy': '+125', 'Wyndham Clark': '+125',
    'Brian Harman': '+130', 'Dustin Johnson': '+130', 'Scottie Scheffler': '-1000', 'Justin Thomas': '-320',
    'Xander Schauffele': '-270', 'Ludvig Aberg': '-210', 'Tommy Fleetwood': '-175', 'Joaquin Niemann': '-165',
    'Tyrrell Hatton': '-150', 'Brooks Koepka': '-130', 'Jordan Spieth': '-125', 'Daniel Berger': '+100',
    'Patrick Reed': '+100', 'Sungjae Im': '+100', 'Keith Mitchell': '+120', 'Justin Rose': '+125',
    'Sam Burns': '+125', 'Akshay Bhatia': '+130', 'Denny McCarthy': '+130', 'Max Homa': '+130'
}

def fetch_odds():
    API_KEY = "7e28b633936a9e47635d45d4efebcede"
    BASE_URL = "https://api.the-odds-api.com/v4/sports"
    
    try:
        # First, get the sport key for golf PGA Championship
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
        
        # Find the golf PGA Championship tournament key
        golf_pga_key = None
        for sport in sports_data:
            if "golf_pga" in sport.get("key", ""):
                golf_pga_key = sport["key"]
                break
        
        if not golf_pga_key:
            print("Could not find PGA Championship tournament in available sports")
            return None
            
        print(f"\nFound PGA Championship key: {golf_pga_key}")
        
        # Get the odds for the tournament
        print("\nFetching tournament odds...")
        odds_response = requests.get(
            f"{BASE_URL}/{golf_pga_key}/odds",
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
            
            # Find FanDuel bookmaker
            fanduel_bookmaker = None
            for bookmaker in event.get("bookmakers", []):
                if bookmaker["title"] == "FanDuel":
                    fanduel_bookmaker = bookmaker
                    break
            
            if fanduel_bookmaker:
                print(f"\nUsing odds from: {fanduel_bookmaker['title']}")
                for market in fanduel_bookmaker.get("markets", []):
                    if market["key"] == "outrights":
                        for outcome in market["outcomes"]:
                            name = outcome["name"]
                            odds = outcome["price"]
                            
                            # Check if we already have this golfer
                            if not any(g["name"] == name for g in golfers):
                                golfers.append({
                                    "name": name,
                                    "win_odds": odds,
                                    "top40_odds": top40_odds_dict.get(name, "N/A"),
                                    "make_cut_odds": "N/A"
                                })
            else:
                print("\nFanDuel odds not found, using first available bookmaker")
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
                                    golfers.append({
                                        "name": name,
                                        "win_odds": odds,
                                        "top40_odds": top40_odds_dict.get(name, "N/A"),
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
        filename = f"pga_championship_odds_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("2025 PGA Championship Odds\n")
            f.write("=" * 50 + "\n\n")
            f.write("Data sourced from The Odds API (FanDuel)\n")
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
    print("Fetching PGA Championship 2025 odds...")
    golfers = fetch_odds()
    filename = save_odds_to_file(golfers)
    if filename:
        print(f"\nTo view the odds, open {filename}")
        print("To update the web interface, copy this file to the web directory")

if __name__ == "__main__":
    main() 