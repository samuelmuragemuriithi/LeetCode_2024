def tally_results(matches):
    team_stats = {}
    
    for match in matches:
        team1, team2, outcome = match.split(';')
        if outcome == 'win':
            winner = team1
            loser = team2
        elif outcome == 'loss':
            winner = team2
            loser = team1
        else:
            continue
        
        # Update winner stats
        team_stats[winner] = team_stats.get(winner, [0, 0, 0, 0, 0])
        team_stats[winner][0] += 1  # Matches Played
        team_stats[winner][1] += 1  # Matches Won
        team_stats[winner][4] += 3  # Points
        
        # Update loser stats
        team_stats[loser] = team_stats.get(loser, [0, 0, 0, 0, 0])
        team_stats[loser][0] += 1  # Matches Played
        team_stats[loser][3] += 1  # Matches Lost
        
    # Convert team_stats dictionary to list of tuples
    team_stats_list = [(team, stats) for team, stats in team_stats.items()]
    
    # Sort the teams based on points and then alphabetically
    team_stats_list.sort(key=lambda x: (-x[1][4], x[0]))
    
    return team_stats_list

# Input matches
matches = [
    "Allegoric Alaskans;Blithering Badgers;win",
    "Devastating Donkeys;Courageous Californians;draw",
    "Devastating Donkeys;Allegoric Alaskans;win",
    "Courageous Californians;Blithering Badgers;loss",
    "Blithering Badgers;Devastating Donkeys;loss",
    "Allegoric Alaskans;Courageous Californians;win"
]

# Tally the results
results = tally_results(matches)

# Print the table
print("Team\t\t| MP | W | D | L | P")
print("-" * 45)
for team, stats in results:
    print(f"{team.ljust(20)} | {stats[0]}  | {stats[1]}  | {stats[0] - stats[1] - stats[3]}  | {stats[3]}  | {stats[4]}")

