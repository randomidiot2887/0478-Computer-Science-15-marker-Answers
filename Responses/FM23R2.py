
#Names of teams
TeamName = [
    "ManchesterUnited",
    "LiverPoll",
    "Arcticius Mandetitus"
]

#points for teams per match
TeamPoints = [
    [3, 3, 2, 1], #For ManchesterUnited
    [0, 0, 1, 0], #LiverPoll
    [1, 2, 3, 0]  #Arcticius Mandetitus
]

#Number of teams
LeagueSize = 3

#No matches played
MatchNo = 4

#3 is a away win
#2 is a home win
#1 is a draw
#0 is a loss

#Calculate total points for each team

#Store total points for each team
Points = [0 for _ in range(LeagueSize)]

for team in range (LeagueSize):
    for match in range(MatchNo):
        Points[team] += TeamPoints[team][match] #Totaling points for teams

#Store statistics for each team
Statistics = [[0 for _ in range(4)] for _ in range(LeagueSize)]

#Counting number of away wins, homewins, drawn matchs and losses
for team in range(LeagueSize):
    for match in range(MatchNo):
        match TeamPoints[team][match]: 
            case 0:#If lost
                Statistics[team][0] += 1
            case 1:#if drawn
                Statistics[team][1] += 1
            case 2:#if home win
                Statistics[team][2] += 1
            case 3:#if away win
                Statistics[team][3] += 1
            case _: print("Error occured in counting")

#Find team with most and least points
Least_Points_team_name = ""
Least_Points_team_score = float("INF")
Most_Points_team_name = ""
Most_Points_team_score = -float("INF")

for team in range(LeagueSize):
    if Least_Points_team_score > Points[team]: #Finding least point
        Least_Points_team_score = Points[team]
        Least_Points_team_name = TeamName[team]
    if Most_Points_team_score < Points[team]: #Finding most points
        Most_Points_team_score = Points[team]
        Most_Points_team_name = TeamName[team]
#Outputting name, total points, and stats for each team
for team in range(LeagueSize):
    print(f"STATS FOR TEAM {TeamName[team]}")
    print(f"Team has a score of {Points[team]}")
    print(f"Team has lost {Statistics[team][0]} time")
    print(f"Team has drawn {Statistics[team][1]} time")
    print(f"Team has home win {Statistics[team][2]} time")
    print(f"Team has away win {Statistics[team][3]} time")
#Win and lost matches
print(f"Team with most points is {Most_Points_team_name}")
print(f"Team with least points is {Least_Points_team_name}")
