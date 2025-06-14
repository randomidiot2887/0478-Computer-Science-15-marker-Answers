import random as r #Imports random library for random number generation
Grid = [[0 for _ in range(5)] for _ in range(5)]#Grid, where X is hidden in
def movedirplayer(diarection_to_move, player_x_cords, player_y_cords):#Handle diarection to move
    diarection_to_move = diarection_to_move.upper()
    match diarection_to_move:
        case 'L':#Move left
            if player_x_cords - 1 == -1:#IF move is invalid
                return 0 #Represents invalid move
            else:
                return 1 #Represents left
        case 'R':#Move right
            if player_x_cords + 1 == 5:#IF move is invalid
                return 0 #Represents invalid move
            else:
                return 10 #Represents right
        case 'U':#Move up
            if player_y_cords - 1 == -1:#IF move is invalid
                return 0 #Represents invalid move
            else:
                return 11 #Represents Up
        case "D":#Move down
            if player_y_cords + 1 == 5:#IF move is invalid
                return 0 #Represents invalid move
            else:
                return 100 #Represents down
        case _:#IF any other value input by stoopid user
            return 101 #Represents an invalid move
#Hide X in a random position in Grid
while True:#Repeats until Grid[0][0] == ""
    x = r.randint(0, 4)#Generates a random value between 0 and 4
    y = r.randint(0, 4)#Generates a random value between 0 and 4
    if not(x == 0 and y == 0):#IF both x and y aint eaqual to 0
        Grid[x][y] = 'X'#Put x in a random position of Grid[]
        break#Exits check (validated)
player_x, player_y = 0, 0 #Make player start at 0, 0
moves = 10 #Player starts with 10 moves
while True:#Repeats until user wins or looses
    valid_move = True#Initialise valid move flag
    print(f"U can move (L)eft, (R)ight, (U)p or (D)own\nU have {moves} Moves left")
    match movedirplayer((input("Input diarection u want to move\n: - ")), player_x, player_y): #Get user input, validate it, and process it out
        case 0: print("Move is not valid, without going out of bounds"); valid_move = False #if move cannot be carried out
        case 1: player_x -= 1 #move left
        case 10: player_x += 1 #Move right
        case 11: player_y -= 1 #move up
        case 100: player_y += 1 #move down
        case 101: print("You can input the following\nD for down\nU for up\nR for right\nL for left"); valid_move = False #invalid option
    if valid_move and Grid[player_x][player_y] == 'X':#If move is valid, and if you found x
        print("You won"); break#Print 'You won' and exits program
    elif valid_move and not(Grid[player_x][player_y] == 'X') and moves == 1:#If valid move, and not found x, and moves are used up
        print("You lost"); break#Print 'you lost' and exits program
    elif valid_move and not(Grid[player_x][player_y] == 'X') and moves != 1: #If valid move and you didnt find x, but u also have spare moves
        moves -= 1#Decrement moves, and go to next cycle