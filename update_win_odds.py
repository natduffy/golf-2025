import os
from datetime import datetime

def read_existing_odds(filename):
    odds_data = {}
    current_golfer = None
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Golfer: '):
                current_golfer = line.replace('Golfer: ', '')
                odds_data[current_golfer] = {'win': 'N/A', 'top20': 'N/A', 'top40': 'N/A'}
            elif line.startswith('Win Odds: '):
                odds_data[current_golfer]['win'] = line.replace('Win Odds: ', '')
            elif line.startswith('Top 20 Odds: '):
                odds_data[current_golfer]['top20'] = line.replace('Top 20 Odds: ', '')
            elif line.startswith('Top 40 Odds: '):
                odds_data[current_golfer]['top40'] = line.replace('Top 40 Odds: ', '')
    return odds_data

def read_new_odds(filename):
    new_win_odds = {}
    current_golfer = None
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if line.startswith('Golfer: '):
            current_golfer = line.replace('Golfer: ', '')
        elif line.startswith('Win Odds: '):
            new_win_odds[current_golfer] = line.replace('Win Odds: ', '')
    
    return new_win_odds

def merge_and_save_odds(existing_odds, new_win_odds, output_file):
    with open(output_file, 'w') as f:
        f.write("2025 Masters Tournament Odds\n")
        f.write("==================================================\n\n")
        f.write("Data sourced from The Odds API and additional sources\n")
        f.write("Note: Make Cut odds may not be available\n\n")
        
        # Sort golfers by win odds (converting to float, handling 'N/A')
        def get_win_odds(golfer):
            odds = new_win_odds.get(golfer, '999999')
            try:
                return float(odds)
            except ValueError:
                return 999999
        
        sorted_golfers = sorted(existing_odds.keys(), key=get_win_odds)
        
        for golfer in sorted_golfers:
            if golfer in new_win_odds:  # Only include golfers with current win odds
                f.write(f"Golfer: {golfer}\n")
                f.write(f"Win Odds: {new_win_odds[golfer]}\n")
                f.write(f"Top 20 Odds: {existing_odds[golfer]['top20']}\n")
                f.write(f"Top 40 Odds: {existing_odds[golfer]['top40']}\n")
                f.write("-" * 30 + "\n")

def normalize_name(name):
    # Remove any leading/trailing whitespace
    name = name.strip()
    
    # Handle special cases
    if name == "Scottie Scheffler":
        return "S.Scheffler"
    elif name == "Rory McIlroy":
        return "R.McIlroy"
    elif name == "Collin Morikawa":
        return "C.Morikawa"
    elif name == "Jon Rahm":
        return "J.Rahm"
    elif name == "Ludvig Aberg":
        return "L.Aberg"
    elif name == "Bryson DeChambeau":
        return "B.DeChambeau"
    elif name == "Xander Schauffele":
        return "X.Schauffele"
    elif name == "Hideki Matsuyama":
        return "H.Matsuyama"
    elif name == "Joaquin Niemann":
        return "J.Niemann"
    elif name == "Patrick Cantlay":
        return "P.Cantlay"
    elif name == "Viktor Hovland":
        return "V.Hovland"
    elif name == "Brooks Koepka":
        return "B.Koepka"
    elif name == "Jordan Spieth":
        return "J.Spieth"
    elif name == "Tommy Fleetwood":
        return "T.Fleetwood"
    elif name == "Tyrrell Hatton":
        return "T.Hatton"
    elif name == "Cameron Smith":
        return "C.Smith"
    elif name == "Min Woo Lee":
        return "K.Lee"  # This appears to be how it's listed in the top 20 odds
    elif name == "Shane Lowry":
        return "S.Lowry"
    elif name == "Will Zalatoris":
        return "W.Zalatoris"
    elif name == "Russell Henley":
        return "R.Henley"
    elif name == "Tony Finau":
        return "T.Finau"
    elif name == "Corey Conners":
        return "C.Conners"
    elif name == "Jason Day":
        return "J.Day"
    elif name == "Sepp Straka":
        return "S.Straka"
    elif name == "Joohyung Kim":
        return "J.Kim"
    elif name == "Wyndham Clark":
        return "W.Clark"
    elif name == "Cameron Young":
        return "C.Young"
    elif name == "Dustin Johnson":
        return "D.Johnson"
    elif name == "Sahith Theegala":
        return "S.Theegala"
    elif name == "Sam Burns":
        return "S.Burns"
    elif name == "Sungjae Im":
        return "S.Im"
    elif name == "Matthew Fitzpatrick":
        return "M.Fitzpatrick"
    elif name == "Daniel Berger":
        return "D.Berger"
    elif name == "Sergio Garcia":
        return "S.Garcia"
    elif name == "Justin Rose":
        return "J.Rose"
    elif name == "Keegan Bradley":
        return "K.Bradley"
    elif name == "Max Homa":
        return "M.Homa"
    return name

def update_top20_odds():
    # Dictionary of new top 20 odds
    new_top20_odds = {
        'S.Scheffler': '-590',
        'R.McIlroy': '-400',
        'J.Rahm': '-159',
        'C.Morikawa': '-175',
        'X.Schauffele': '-137',
        'B.DeChambeau': '-137',
        'L.Aberg': '-110',
        'J.Niemann': '110',
        'H.Matsuyama': '130',
        'J.Spieth': '130',
        'T.Fleetwood': '130',
        'B.Koepka': '130',
        'S.Lowry': '130',
        'P.Cantlay': '130',
        'V.Hovland': '130',
        'T.Hatton': '160',
        'R.Henley': '160',
        'W.Zalatoris': '175',
        'K.Lee': '175',
        'R.MacIntyre': '175',
        'C.Smith': '175',
        'C.Conners': '250',
        'S.Straka': '250',
        'T.Finau': '250',
        'J.Day': '250',
        'W.Clark': '300',
        'S.Garcia': '300',
        'K.Bradley': '300',
        'S.Burns': '300',
        'J.Kim': '300',
        'S.Theegala': '300',
        'D.Johnson': '300',
        'M.Fitzpatrick': '335',
        'D.Berger': '375',
        'J.Rose': '375',
        'A.Rai': '375',
        'S.Im': '375',
        'A.Scott': '400',
        'D.Thompson': '400',
        'T.Pendrith': '400',
        'B.Horschel': '375',
        'M.McNealy': '375',
        'T.Detry': '400',
        'L.Glover': '500',
        'M.Kim': '400',
        'B.Harman': '400',
        'N.Hojgaard': '400',
        'D.McCarthy': '500',
        'J.Spaun': '500',
        'H.English': '500',
        'C.Young': '375',
        'P.Mickelson': '500',
        'M.Homa': '500',
        'L.List': '650',
        'J.Poston': '650',
        'C.Bezuidenhout': '650',
        'C.Davis': '550',
        'N.Dunlap': '550',
        'N.Echavarria': '550',
        'S.Jaeger': '450',
        'J.Highsmith': '450',
        'K.Yu': '500',
        'A.Eckroat': '550',
        'L.Griffin': '550',
        'J.Vegas': '750',
        'M.McCarty': '600',
        'B.Riley': '850',
        'B.Watson': '850',
        'C.Schwartzel': '700',
        'P.Kizzire': '1100',
        'T.Lawrence': '1200',
        'Z.Johnson': '850',
        'M.Pavon': '850',
        'D.Whitnell': '900',
        'J.Knapp': '1000',
        'B.Campbell': '1000',
        'H.Tai': '2500',
        'E.Beck': '2000',
        'B.Lange': '2000',
        'R.Campos': '2000',
        'V.Singh': '2500',
        'M.Weir': '2500',
        'F.Couples': '2500'
    }
    
    # Read existing odds
    existing_odds = read_existing_odds('masters_odds_20250404_135122.txt')
    
    # Create new file with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f'masters_odds_{timestamp}.txt'
    
    with open(new_filename, 'w') as f:
        for golfer, odds in existing_odds.items():
            normalized_name = normalize_name(golfer)
            f.write(f'Golfer: {golfer}\n')
            f.write(f'Win Odds: {odds["win"]}\n')
            
            # Update top 20 odds if available in new data
            top20 = new_top20_odds.get(normalized_name, 'N/A')
            f.write(f'Top 20 Odds: {top20}\n')
            
            f.write(f'Top 40 Odds: {odds["top40"]}\n\n')
    
    return new_filename

def main():
    # Find the most recent existing odds file
    existing_file = "masters_odds_20250403_121028.txt"  # File with Top 20 and Top 40 odds
    new_odds_file = "masters_odds_20250404_134947.txt"  # File with new win odds
    
    # Read existing odds
    print("Reading existing odds data...")
    existing_odds = read_existing_odds(existing_file)
    
    # Read new win odds
    print("Reading new win odds...")
    new_win_odds = read_new_odds(new_odds_file)
    
    # Create output filename with current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"masters_odds_{timestamp}.txt"
    
    # Merge and save
    print("Merging odds and saving...")
    merge_and_save_odds(existing_odds, new_win_odds, output_file)
    print(f"Updated odds saved to {output_file}")

if __name__ == "__main__":
    new_file = update_top20_odds()
    print(f'Updated odds saved to: {new_file}') 