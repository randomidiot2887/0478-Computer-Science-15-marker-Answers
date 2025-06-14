Clubs = ["" for _ in range(12)]
Statistics = [[0 for _ in range(3)] for _ in range(12)]
Points = [0 for _ in range(12)]

#Points award rate
a_win = 12 #12 Points
a_draw = 5 #5 Points
a_loss = 0 #0 Points

num_playedMetches = 0
#Getting the number of matches played
while True:#VALIDATION CHECK
    num_playedMetches = int(input("Input the number of matches played (MAX 22 Matches)\n: - "))#Gettibg the number of matches played, AS AN INTEGER
    if num_playedMetches > 22:#If input value too much
        print("The maximum amount of matches that can be played is 22")
    if num_playedMetches <= 0:#If input value too less
        print("At least 1 match needs to be played")
    if num_playedMetches > 0 and num_playedMetches <= 22: #IF value is acceptable
        print("Number of matches have been input")
        break#Exit the loop
#Get the names of the clubs
print("Enter the names of the 12 cricket clubs")
for crick_club in range(12):#For each club
    Clubs[crick_club] = input(f"Input the name of club number {crick_club}\n: - ")#Get their name
#Get the number of wins, losses, and drawn matches
for crick_club in range(12):
    while True:#For each club
        print(f"Input stats for {Clubs[crick_club]}")
        Statistics[crick_club][0] = int(input("No Matches Won: - "))#Get the number of wins
        Statistics[crick_club][1] = int(input("No Matches Drawn: - "))#Get the number of drawn matches
        Statistics[crick_club][2] = int(input("No Matches Lost: - "))#Get the number of lost matches
        if Statistics[crick_club][0] + Statistics[crick_club][1] + Statistics[crick_club][2] == num_playedMetches:#Get the total of win, lost and drawn matches, and compare to total matches
            print("Statistics have been input succesfully")#If theyre eaqual, diskplay a msg and leave loop
            Points[crick_club] = Statistics[crick_club][1] * a_draw + Statistics[crick_club][0] * a_win#Total the score of the matches
            break
        else:
            print("Input values have failed verification. Youll need to reenter correct values")#Else warn
#get the cricket club/clubs with most points
most_points = -float("inf")#Initialise to negative infinity
for crick_club in range(12):#For each club
    if most_points < Points[crick_club]:#Check if their score is larger then most_points
        most_points = Points[crick_club]#Assign that to most_points
#Display names of all clubs that win
for each_club in range(12):#For each club
    if Points[each_club] == most_points:#Check if they have most points
        print(f"{Clubs[each_club]} has won with {Statistics[each_club][0]} wins and {Points[each_club]} points total")#If so, print them as a winning club
#End the algorithm
    