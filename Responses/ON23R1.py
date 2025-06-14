Evening = [[False for _ in range(20)] for _ in range(10)]
#Booking seats
def booking(booked_seats):
    while True: #Booking and validating amont of seats
        no_seats = int(input("You can book at most, 4 seats at a time\nInput the number of seats u wanna book\n: - "))
        if no_seats <= 4 and no_seats > 0:
            print("<Seats were booked>")
            return no_seats #Returns number of seats booked
        else:
            print("!Booking failed. booked too much or too less seats!")
#Assigning seats to users
def assign_seats(booked_seats, no_seats_to_book):
    for book in range(no_seats_to_book):#For each seat that needs to be booked.
        booked = False #Some shitty way to stop it from assigning a biollion seats at once
        for row in range(10):
            for seat in range(20):
                if booked:#Makes it not run, if seat has been booked
                    break
                if Evening[row][seat] == False: #IF the seat is empty, book it
                    booked = True
                    Evening[row][seat] = True
                    print(f"<<Seat R{row+1}S{seat+1} has been booked>>")#Tell the user about it with seat and row numbers
            if booked:#HACK
                break
        
    return booked_seats
#Checking if the seats are avalable to book
def check_seat_avalability(booked_seats, no_seats_to_book, total_rows, seats_per_row):
    house_full = False #House will not be full on statup
    limited_seat_amount = False #Theres enough seats for booking to suceed
    if booked_seats >= (total_rows * seats_per_row): #If all seats have been booked
        house_full = True #No seats left
    if (booked_seats + no_seats_to_book) > (total_rows * seats_per_row): #If seats are avalable
        limited_seat_amount = True #Not sufficient seats left to fulfill order
    no_seats_left = (total_rows * seats_per_row) - booked_seats #find amount of seats remaining
    return [house_full, limited_seat_amount, no_seats_left] #Returns a list with the needed data

#Check at the start how many seats are already booked
def check_already_booked():
    no_booked_seats = 0
    for row in range(10):
        for seat in range(20):
            if Evening[row][seat] == True:
                no_booked_seats += 1
    return no_booked_seats

while True:
    seats = check_already_booked()#count number of seats already booked
    if check_seat_avalability(seats, 0, 10, 20)[0]:#if no more seats are avalable
        print("!!House full, cannot book any more seats!!")
        break#Exits the code
    else:
        while True:
            print("Welcome to eff you therer\nDrama students will be performing for one evening")
            num_seats_to_book = booking(seats) #To handle booking
            if check_seat_avalability(seats, num_seats_to_book, 10, 20)[1]: #If insufficient seats, warn and orevent booking
                print("<!Insufficient amount of seats left. booking failed!>")
                print(f"<Theres only {check_seat_avalability(seats, 0, 10, 20)[2]} seats left>")
            else:#If seats are avalable
                assign_seats(seats, num_seats_to_book) #assigns seats to person, reports ticket numbers
                seats += num_seats_to_book #Increments Seats
            break #exits, and restarts the block