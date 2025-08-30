"""
Complete fantasy football player data from master list
All 95 players with positions, teams, projected points, and flags
"""

SAMPLE_PLAYERS = [
    {
        'rank': 1,
        'name': 'Saquon Barkley',
        'position': 'RB',
        'team': 'Phi',
        'projected_points': 343.5,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 1
    },
    {
        'rank': 2,
        'name': 'Bijan Robinson',
        'position': 'RB',
        'team': 'Atl',
        'projected_points': 343.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 2
    },
    {
        'rank': 3,
        'name': 'Christian McCaffrey',
        'position': 'RB',
        'team': 'SF',
        'projected_points': 318.5,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 3
    },
    {
        'rank': 4,
        'name': 'Jahmyr Gibbs',
        'position': 'RB',
        'team': 'Det',
        'projected_points': 318.6,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 4
    },
    {
        'rank': 5,
        'name': 'Jonathan Taylor',
        'position': 'RB',
        'team': 'Ind',
        'projected_points': 322.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 5
    },
    {
        'rank': 6,
        'name': 'Josh Jacobs',
        'position': 'RB',
        'team': 'GB',
        'projected_points': 297.9,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 6
    },
    {
        'rank': 7,
        'name': 'Ashton Jeanty',
        'position': 'RB',
        'team': 'LV',
        'projected_points': 300.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 7
    },
    {
        'rank': 8,
        'name': 'De\'Von Achane',
        'position': 'RB',
        'team': 'Mia',
        'projected_points': 297.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 8
    },
    {
        'rank': 9,
        'name': 'Kyren Williams',
        'position': 'RB',
        'team': 'LAR',
        'projected_points': 299.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 9
    },
    {
        'rank': 10,
        'name': 'Bucky Irving',
        'position': 'RB',
        'team': 'TB',
        'projected_points': 288.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 10
    },
    {
        'rank': 11,
        'name': 'Chase Brown',
        'position': 'RB',
        'team': 'Cin',
        'projected_points': 279.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 11
    },
    {
        'rank': 12,
        'name': 'Ja\'Marr Chase',
        'position': 'WR',
        'team': 'Cin',
        'projected_points': 280.6,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 1
    },
    {
        'rank': 13,
        'name': 'Justin Jefferson',
        'position': 'WR',
        'team': 'Min',
        'projected_points': 266.3,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 2
    },
    {
        'rank': 14,
        'name': 'CeeDee Lamb',
        'position': 'WR',
        'team': 'Dal',
        'projected_points': 256.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 3
    },
    {
        'rank': 15,
        'name': 'Puka Nacua',
        'position': 'WR',
        'team': 'LAR',
        'projected_points': 255.4,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 4
    },
    {
        'rank': 16,
        'name': 'Amon-Ra St. Brown',
        'position': 'WR',
        'team': 'Det',
        'projected_points': 231.9,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 5
    },
    {
        'rank': 17,
        'name': 'Malik Nabers',
        'position': 'WR',
        'team': 'NYG',
        'projected_points': 246.6,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 6
    },
    {
        'rank': 18,
        'name': 'Derrick Henry',
        'position': 'RB',
        'team': 'Bal',
        'projected_points': 314.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 12
    },
    {
        'rank': 19,
        'name': 'James Cook',
        'position': 'RB',
        'team': 'Buf',
        'projected_points': 284.4,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 13
    },
    {
        'rank': 20,
        'name': 'Alvin Kamara',
        'position': 'RB',
        'team': 'NO',
        'projected_points': 254.5,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 14
    },
    {
        'rank': 21,
        'name': 'Tony Pollard',
        'position': 'RB',
        'team': 'Ten',
        'projected_points': 214.3,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 15
    },
    {
        'rank': 22,
        'name': 'Omarion Hampton',
        'position': 'RB',
        'team': 'LAC',
        'projected_points': 270.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 16
    },
    {
        'rank': 23,
        'name': 'Kenneth Walker III',
        'position': 'RB',
        'team': 'Sea',
        'projected_points': 273.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 17
    },
    {
        'rank': 24,
        'name': 'Joe Mixon',
        'position': 'RB',
        'team': 'Hou',
        'projected_points': 206.0,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 18
    },
    {
        'rank': 25,
        'name': 'Breece Hall',
        'position': 'RB',
        'team': 'NYJ',
        'projected_points': 227.9,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 19
    },
    {
        'rank': 26,
        'name': 'D\'Andre Swift',
        'position': 'RB',
        'team': 'Chi',
        'projected_points': 237.3,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 20
    },
    {
        'rank': 27,
        'name': 'TreVeyon Henderson',
        'position': 'RB',
        'team': 'NE',
        'projected_points': 227.4,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 21
    },
    {
        'rank': 28,
        'name': 'James Conner',
        'position': 'RB',
        'team': 'Ari',
        'projected_points': 256.2,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 22
    },
    {
        'rank': 29,
        'name': 'Brock Bowers',
        'position': 'TE',
        'team': 'LV',
        'projected_points': 206.2,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 1
    },
    {
        'rank': 30,
        'name': 'Trey McBride',
        'position': 'TE',
        'team': 'Ari',
        'projected_points': 202.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 2
    },
    {
        'rank': 31,
        'name': 'Tyreek Hill',
        'position': 'WR',
        'team': 'Mia',
        'projected_points': 216.1,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 7
    },
    {
        'rank': 32,
        'name': 'Tee Higgins',
        'position': 'WR',
        'team': 'Cin',
        'projected_points': 217.4,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 8
    },
    {
        'rank': 33,
        'name': 'Davante Adams',
        'position': 'WR',
        'team': 'LAR',
        'projected_points': 214.4,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 9
    },
    {
        'rank': 34,
        'name': 'Ladd McConkey',
        'position': 'WR',
        'team': 'LAC',
        'projected_points': 205.3,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 10
    },
    {
        'rank': 35,
        'name': 'A.J. Brown',
        'position': 'WR',
        'team': 'Phi',
        'projected_points': 229.9,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 11
    },
    {
        'rank': 36,
        'name': 'Nico Collins',
        'position': 'WR',
        'team': 'Hou',
        'projected_points': 229.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 12
    },
    {
        'rank': 37,
        'name': 'Jaxon Smith-Njigba',
        'position': 'WR',
        'team': 'Sea',
        'projected_points': 195.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 13
    },
    {
        'rank': 38,
        'name': 'Terry McLaurin',
        'position': 'WR',
        'team': 'Wsh',
        'projected_points': 203.9,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 14
    },
    {
        'rank': 39,
        'name': 'Garrett Wilson',
        'position': 'WR',
        'team': 'NYJ',
        'projected_points': 194.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 15
    },
    {
        'rank': 40,
        'name': 'Mike Evans',
        'position': 'WR',
        'team': 'TB',
        'projected_points': 196.9,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 16
    },
    {
        'rank': 41,
        'name': 'Marvin Harrison Jr.',
        'position': 'WR',
        'team': 'Ari',
        'projected_points': 198.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 17
    },
    {
        'rank': 42,
        'name': 'Xavier Worthy',
        'position': 'WR',
        'team': 'KC',
        'projected_points': 204.4,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 18
    },
    {
        'rank': 43,
        'name': 'DK Metcalf',
        'position': 'WR',
        'team': 'Pit',
        'projected_points': 199.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 19
    },
    {
        'rank': 44,
        'name': 'DJ Moore',
        'position': 'WR',
        'team': 'Chi',
        'projected_points': 194.3,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 20
    },
    {
        'rank': 45,
        'name': 'Zay Flowers',
        'position': 'WR',
        'team': 'Bal',
        'projected_points': 195.3,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 21
    },
    {
        'rank': 46,
        'name': 'Courtland Sutton',
        'position': 'WR',
        'team': 'Den',
        'projected_points': 190.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 22
    },
    {
        'rank': 47,
        'name': 'Calvin Ridley',
        'position': 'WR',
        'team': 'Ten',
        'projected_points': 195.2,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 23
    },
    {
        'rank': 48,
        'name': 'DeVonta Smith',
        'position': 'WR',
        'team': 'Phi',
        'projected_points': 178.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 24
    },
    {
        'rank': 49,
        'name': 'Jaylen Waddle',
        'position': 'WR',
        'team': 'Mia',
        'projected_points': 182.1,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 25
    },
    {
        'rank': 50,
        'name': 'Jerry Jeudy',
        'position': 'WR',
        'team': 'Cle',
        'projected_points': 187.6,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 26
    },
    {
        'rank': 51,
        'name': 'Jameson Williams',
        'position': 'WR',
        'team': 'Det',
        'projected_points': 185.6,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 27
    },
    {
        'rank': 52,
        'name': 'George Pickens',
        'position': 'WR',
        'team': 'Dal',
        'projected_points': 183.9,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 28
    },
    {
        'rank': 53,
        'name': 'Sam LaPorta',
        'position': 'TE',
        'team': 'Det',
        'projected_points': 154.1,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 3
    },
    {
        'rank': 54,
        'name': 'Rome Odunze',
        'position': 'WR',
        'team': 'Chi',
        'projected_points': 181.6,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 29
    },
    {
        'rank': 55,
        'name': 'Tetairoa McMillan',
        'position': 'WR',
        'team': 'Car',
        'projected_points': 176.4,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 30
    },
    {
        'rank': 56,
        'name': 'Travis Hunter',
        'position': 'WR',
        'team': 'Jax',
        'projected_points': 197.9,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 31
    },
    {
        'rank': 57,
        'name': 'David Montgomery',
        'position': 'RB',
        'team': 'Det',
        'projected_points': 220.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 23
    },
    {
        'rank': 58,
        'name': 'Aaron Jones Sr.',
        'position': 'RB',
        'team': 'Min',
        'projected_points': 208.7,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 24
    },
    {
        'rank': 59,
        'name': 'T.J. Hockenson',
        'position': 'TE',
        'team': 'Min',
        'projected_points': 146.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 4
    },
    {
        'rank': 60,
        'name': 'RJ Harvey',
        'position': 'RB',
        'team': 'Den',
        'projected_points': 201.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 25
    },
    {
        'rank': 61,
        'name': 'Isiah Pacheco',
        'position': 'RB',
        'team': 'KC',
        'projected_points': 214.6,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 26
    },
    {
        'rank': 62,
        'name': 'Chris Godwin',
        'position': 'WR',
        'team': 'TB',
        'projected_points': 156.1,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 32
    },
    {
        'rank': 63,
        'name': 'Jakobi Meyers',
        'position': 'WR',
        'team': 'LV',
        'projected_points': 174.6,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 33
    },
    {
        'rank': 64,
        'name': 'Chris Olave',
        'position': 'WR',
        'team': 'NO',
        'projected_points': 165.2,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 34
    },
    {
        'rank': 65,
        'name': 'Cooper Kupp',
        'position': 'WR',
        'team': 'Sea',
        'projected_points': 163.3,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 35
    },
    {
        'rank': 66,
        'name': 'Stefon Diggs',
        'position': 'WR',
        'team': 'NE',
        'projected_points': 159.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 36
    },
    {
        'rank': 67,
        'name': 'Matthew Golden',
        'position': 'WR',
        'team': 'GB',
        'projected_points': 169.8,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 37
    },
    {
        'rank': 68,
        'name': 'Jordan Addison',
        'position': 'WR',
        'team': 'Min',
        'projected_points': 145.2,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 38
    },
    {
        'rank': 69,
        'name': 'Tyrone Tracy Jr.',
        'position': 'RB',
        'team': 'NYG',
        'projected_points': 212.5,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 27
    },
    {
        'rank': 70,
        'name': 'Jaylen Warren',
        'position': 'RB',
        'team': 'Pit',
        'projected_points': 195.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 28
    },
    {
        'rank': 71,
        'name': 'Kaleb Johnson',
        'position': 'RB',
        'team': 'Pit',
        'projected_points': 204.3,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 29
    },
    {
        'rank': 72,
        'name': 'Travis Kelce',
        'position': 'TE',
        'team': 'KC',
        'projected_points': 140.0,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 5
    },
    {
        'rank': 73,
        'name': 'David Njoku',
        'position': 'TE',
        'team': 'Cle',
        'projected_points': 140.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 6
    },
    {
        'rank': 74,
        'name': 'Mark Andrews',
        'position': 'TE',
        'team': 'Bal',
        'projected_points': 140.5,
        'risk_flag': True,
        'undervalued_flag': True,
        'position_rank': 7
    },
    {
        'rank': 75,
        'name': 'Evan Engram',
        'position': 'TE',
        'team': 'Den',
        'projected_points': 129.3,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 8
    },
    {
        'rank': 76,
        'name': 'Quinshon Judkins',
        'position': 'RB',
        'team': 'Cle',
        'projected_points': 206.2,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 30
    },
    {
        'rank': 77,
        'name': 'Brian Robinson Jr.',
        'position': 'RB',
        'team': 'Wsh',
        'projected_points': 206.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 31
    },
    {
        'rank': 78,
        'name': 'J.K. Dobbins',
        'position': 'RB',
        'team': 'Den',
        'projected_points': 173.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 32
    },
    {
        'rank': 79,
        'name': 'Rhamondre Stevenson',
        'position': 'RB',
        'team': 'NE',
        'projected_points': 181.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 33
    },
    {
        'rank': 80,
        'name': 'Javonte Williams',
        'position': 'RB',
        'team': 'Dal',
        'projected_points': 163.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 34
    },
    {
        'rank': 81,
        'name': 'Khalil Shakir',
        'position': 'WR',
        'team': 'Buf',
        'projected_points': 165.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 39
    },
    {
        'rank': 82,
        'name': 'Jauan Jennings',
        'position': 'WR',
        'team': 'SF',
        'projected_points': 164.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 40
    },
    {
        'rank': 83,
        'name': 'Deebo Samuel',
        'position': 'WR',
        'team': 'Wsh',
        'projected_points': 169.7,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 41
    },
    {
        'rank': 84,
        'name': 'Ricky Pearsall',
        'position': 'WR',
        'team': 'SF',
        'projected_points': 154.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 42
    },
    {
        'rank': 85,
        'name': 'Keon Coleman',
        'position': 'WR',
        'team': 'Buf',
        'projected_points': 155.5,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 43
    },
    {
        'rank': 86,
        'name': 'Michael Pittman Jr.',
        'position': 'WR',
        'team': 'Ind',
        'projected_points': 142.6,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 44
    },
    {
        'rank': 87,
        'name': 'Jayden Reed',
        'position': 'WR',
        'team': 'GB',
        'projected_points': 138.2,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 45
    },
    {
        'rank': 88,
        'name': 'Keenan Allen',
        'position': 'WR',
        'team': 'LAC',
        'projected_points': 149.2,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 46
    },
    {
        'rank': 89,
        'name': 'Darnell Mooney',
        'position': 'WR',
        'team': 'Atl',
        'projected_points': 131.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 47
    },
    {
        'rank': 90,
        'name': 'Josh Downs',
        'position': 'WR',
        'team': 'Ind',
        'projected_points': 128.8,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 48
    },
    {
        'rank': 91,
        'name': 'Rashid Shaheed',
        'position': 'WR',
        'team': 'NO',
        'projected_points': 153.4,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 49
    },
    {
        'rank': 92,
        'name': 'Jayden Higgins',
        'position': 'WR',
        'team': 'Hou',
        'projected_points': 128.5,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 50
    },
    {
        'rank': 93,
        'name': 'Emeka Egbuka',
        'position': 'WR',
        'team': 'TB',
        'projected_points': 125.6,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 51
    },
    {
        'rank': 94,
        'name': 'Tucker Kraft',
        'position': 'TE',
        'team': 'GB',
        'projected_points': 128.7,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 52
    },
    {
        'rank': 95,
        'name': 'Austin Ekeler',
        'position': 'RB',
        'team': 'Wsh',
        'projected_points': 147.1,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 35
    }
]

# Add missing players to the end of the list
MISSING_PLAYERS = [
    # Quarterbacks
    {
        'rank': 96,
        'name': 'Lamar Jackson',
        'position': 'QB',
        'team': 'Bal',
        'projected_points': 380.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 1
    },
    {
        'rank': 97,
        'name': 'Josh Allen',
        'position': 'QB',
        'team': 'Buf',
        'projected_points': 375.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 2
    },
    {
        'rank': 98,
        'name': 'Patrick Mahomes',
        'position': 'QB',
        'team': 'KC',
        'projected_points': 370.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 3
    },
    {
        'rank': 99,
        'name': 'Jalen Hurts',
        'position': 'QB',
        'team': 'Phi',
        'projected_points': 365.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 4
    },
    {
        'rank': 100,
        'name': 'Justin Herbert',
        'position': 'QB',
        'team': 'LAC',
        'projected_points': 360.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 5
    },
    {
        'rank': 101,
        'name': 'Kyler Murray',
        'position': 'QB',
        'team': 'Ari',
        'projected_points': 355.0,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 6
    },
    {
        'rank': 102,
        'name': 'C.J. Stroud',
        'position': 'QB',
        'team': 'Hou',
        'projected_points': 350.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 7
    },
    {
        'rank': 103,
        'name': 'J.J. McCarthy',
        'position': 'QB',
        'team': 'Min',
        'projected_points': 345.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 8
    },
    # Additional Running Backs
    {
        'rank': 104,
        'name': 'Nick Chubb',
        'position': 'RB',
        'team': 'Cle',
        'projected_points': 200.0,
        'risk_flag': True,
        'undervalued_flag': False,
        'position_rank': 36
    },
    {
        'rank': 105,
        'name': 'Cam Akers',
        'position': 'RB',
        'team': 'Min',
        'projected_points': 180.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 37
    },
    {
        'rank': 106,
        'name': 'Travis Etienne',
        'position': 'RB',
        'team': 'Jax',
        'projected_points': 175.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 38
    },
    {
        'rank': 107,
        'name': 'Will Shipley',
        'position': 'RB',
        'team': 'Phi',
        'projected_points': 170.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 39
    },
    {
        'rank': 108,
        'name': 'Tank Bigsby',
        'position': 'RB',
        'team': 'Jax',
        'projected_points': 165.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 40
    },
    {
        'rank': 109,
        'name': 'Jaydon Blue',
        'position': 'RB',
        'team': 'Dal',
        'projected_points': 160.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 41
    },
    {
        'rank': 110,
        'name': 'Woody Marks',
        'position': 'RB',
        'team': 'Hou',
        'projected_points': 155.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 42
    },
    # Additional Wide Receivers
    {
        'rank': 111,
        'name': 'Brandon Aiyuk',
        'position': 'WR',
        'team': 'SF',
        'projected_points': 170.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 55
    },
    {
        'rank': 112,
        'name': 'Tyler Lockett',
        'position': 'WR',
        'team': 'Sea',
        'projected_points': 165.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 56
    },
    {
        'rank': 113,
        'name': 'Marvin Mims',
        'position': 'WR',
        'team': 'Den',
        'projected_points': 160.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 57
    },
    {
        'rank': 114,
        'name': 'Roman Wilson',
        'position': 'WR',
        'team': 'Pit',
        'projected_points': 155.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 58
    },
    {
        'rank': 115,
        'name': 'DeMario Douglas',
        'position': 'WR',
        'team': 'NE',
        'projected_points': 150.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 59
    },
    {
        'rank': 116,
        'name': 'Quentin Johnston',
        'position': 'WR',
        'team': 'LAC',
        'projected_points': 145.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 60
    },
    # Additional Tight Ends
    {
        'rank': 117,
        'name': 'George Kittle',
        'position': 'TE',
        'team': 'SF',
        'projected_points': 120.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 11
    },
    {
        'rank': 118,
        'name': 'Zach Ertz',
        'position': 'TE',
        'team': 'Ari',
        'projected_points': 110.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 12
    },
    {
        'rank': 119,
        'name': 'Kyle Pitts',
        'position': 'TE',
        'team': 'Atl',
        'projected_points': 105.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 13
    },
    {
        'rank': 120,
        'name': 'Brenton Strange',
        'position': 'TE',
        'team': 'Jax',
        'projected_points': 100.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 14
    },
    {
        'rank': 121,
        'name': 'Theo Johnson',
        'position': 'TE',
        'team': 'NYG',
        'projected_points': 95.0,
        'risk_flag': False,
        'undervalued_flag': True,
        'position_rank': 15
    },
    # Kickers
    {
        'rank': 122,
        'name': 'Justin Tucker',
        'position': 'K',
        'team': 'Bal',
        'projected_points': 150.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 1
    },
    {
        'rank': 123,
        'name': 'Harrison Butker',
        'position': 'K',
        'team': 'KC',
        'projected_points': 145.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 2
    },
    # Team Defenses
    {
        'rank': 124,
        'name': 'Buffalo Bills',
        'position': 'DEF',
        'team': 'Buf',
        'projected_points': 120.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 1
    },
    {
        'rank': 125,
        'name': 'Philadelphia Eagles',
        'position': 'DEF',
        'team': 'Phi',
        'projected_points': 115.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 2
    },
    {
        'rank': 126,
        'name': 'Denver Broncos',
        'position': 'DEF',
        'team': 'Den',
        'projected_points': 110.0,
        'risk_flag': False,
        'undervalued_flag': False,
        'position_rank': 3
    }
]

# Combine the original players with missing players
ALL_PLAYERS = SAMPLE_PLAYERS + MISSING_PLAYERS

def get_sample_players():
    """Return complete player data including missing players"""
    return ALL_PLAYERS.copy()

def get_player_stats():
    """Return statistics about the player dataset"""
    total_players = len(SAMPLE_PLAYERS)
    positions = {}
    teams = set()
    high_risk = 0
    undervalued = 0
    
    for player in SAMPLE_PLAYERS:
        # Count positions
        pos = player['position']
        positions[pos] = positions.get(pos, 0) + 1
        
        # Count teams
        teams.add(player['team'])
        
        # Count flags
        if player['risk_flag']:
            high_risk += 1
        if player['undervalued_flag']:
            undervalued += 1
    
    return {
        'total_players': total_players,
        'positions': positions,
        'unique_teams': len(teams),
        'high_risk_players': high_risk,
        'undervalued_players': undervalued,
        'avg_projected_points': sum(p['projected_points'] for p in SAMPLE_PLAYERS) / total_players
    }

def get_players_by_position(position):
    """Return all players for a specific position"""
    return [p for p in SAMPLE_PLAYERS if p['position'] == position]

def get_high_risk_players():
    """Return all high-risk players (🚩)"""
    return [p for p in SAMPLE_PLAYERS if p['risk_flag']]

def get_undervalued_players():
    """Return all undervalued players (💎)"""
    return [p for p in SAMPLE_PLAYERS if p['undervalued_flag']]

def get_players_by_team(team):
    """Return all players for a specific team"""
    return [p for p in SAMPLE_PLAYERS if p['team'] == team]

def search_players(query):
    """Search players by name or team (case-insensitive)"""
    query = query.lower()
    return [p for p in SAMPLE_PLAYERS 
            if query in p['name'].lower() or query in p['team'].lower()]

def get_top_players_by_position(position, limit=10):
    """Get top players by projected points for a specific position"""
    position_players = get_players_by_position(position)
    return sorted(position_players, key=lambda x: x['projected_points'], reverse=True)[:limit]

def get_position_breakdown():
    """Get detailed breakdown of players by position"""
    breakdown = {}
    for player in SAMPLE_PLAYERS:
        pos = player['position']
        if pos not in breakdown:
            breakdown[pos] = {
                'count': 0,
                'total_points': 0,
                'high_risk': 0,
                'undervalued': 0,
                'players': []
            }
        
        breakdown[pos]['count'] += 1
        breakdown[pos]['total_points'] += player['projected_points']
        if player['risk_flag']:
            breakdown[pos]['high_risk'] += 1
        if player['undervalued_flag']:
            breakdown[pos]['undervalued'] += 1
        breakdown[pos]['players'].append(player)
    
    # Calculate averages
    for pos in breakdown:
        breakdown[pos]['avg_points'] = breakdown[pos]['total_points'] / breakdown[pos]['count']
    
    return breakdown
