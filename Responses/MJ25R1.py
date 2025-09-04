# Declare the required data scructures
CompetitorName = ['' for _ in range(25)]
CompetitorScore = [[0 for _ in range(5)] for _ in range(25)]


# getting input of scores
print('Input the scores for members for each of the 5 events')
for member in range(25): # Repeats per member
    print(f"Input the scores for {CompetitorName[member]} for:")
    for event in range(5): # Repeats oer event
        while True: # Validates score, after getting input
            score = int(input(f'Event {event+1}:')) # gets score as input
            if score >= 0 and score <= 100: # If the score withn 0 <= x <= 100
                CompetitorScore[member][event] = score # Store score in list
                break # Exits validation check
            else: # if score out of range, print error msg
                print('Please enter a score between 0 and 100 inclusive')

# Calculating highest points for each event
highest_scores = [-1 for _ in range(5)] # Stores high scores
for member in range(25): # Repeats for all members
    for event in range(5): # Repeats for all event
        if highest_scores[event] < CompetitorScore[member][event]: # If members score is more then highest score
            highest_scores[event] = CompetitorScore[member][event] # Update largest score with value

# Calculate total points for all members
total_score = [0 for _ in range(25)]
top_score = -1
for member in range(25):
    # Totals the score per member for event
    for event in range(5): total_score[member] += CompetitorScore[member][event] 
    # Check if score is highest
    if top_score < total_score[member]:
        top_score = total_score[member] # Update top scor with top score value

"""
Prints the following info
 - Competitors who scored highest score for each event
 - Competitors who scored highest total score across all events
"""

for member in range(25):
    if total_score[member] == top_score: # if the cmpetitor has highest total score across all events
        print(f'Competitor {CompetitorName[member]} has scored most total points')
    for event in range(5):
        if CompetitorScore[member][event] == highest_scores[event]: # if the competitor has highest score in an event
            print(f'Competitor {CompetitorName[member]} has achived highest score in event {event+1}')