MemberID = ["" for _ in range(1000)]
Name = [["" for _ in range(2)] for _ in range(1000)]

def verify_member_id(Id_of_new_member):#verify memberID
    while True:#Repeats until
        length = True#Sets length check to true
        unique_id = True#Says id is unique or not
        if len(Id_of_new_member) == 6:#IF id is 6 chars
            for member in MemberID:#for all members
                if member == Id_of_new_member:#If the new id is not unique
                    unique_id = False#set flag to false
                    break#Exit that block
        else:#If id is not unique
            length = False#Set check to false
        if not length or not unique_id:#if wither check fails
            #Prompt and get new details
            print("Please reenter memberID, as the enterd one didnt match requrinments")
            Id_of_new_member = input(": - ")
        if unique_id and length:#If unique and 6 chars
                return Id_of_new_member#Returns ID
def add_new_member():#Adding new mmeber
    print("MemberID must be 6 charectors long, and be unique")#Giving constrains
    NewID = verify_member_id(input("Input new memberID: - "))#Get and verify memberID
    Name_person_f = input("Input your first name: - ")#get name first
    Name_person_l = input("Input your last name: - ")#get name last
    for member in range(len(MemberID)):#Fir each member
        if MemberID[member] == "":#Find first empty space
            #Store data in list
            Name[member][0] = Name_person_f
            MemberID[member] = NewID
            Name[member][1] = Name_person_l
            break#Exit loop
    print("Data entry sucess\nUser datails enterd")#Msg, endf of function

def display_all_mmebers():#Dispaky all mem bers degtails
    print("Displaying all members in system...")
    for person in range(1000):#For everybody
        if MemberID[person] != "":#If the element is not empty
            print(f"{MemberID[person]}: {Name[person][0]} {Name[person][1]}")#Display their details (fMembership ID : First name Last name)
exit = False#Set exit flag to false
while not exit:#While not exit
    #Show info and main menu
    print("Welcome to club manager")
    print("Main menu")
    print("1: Add new member")
    print("2: Display list of all members")
    print("3: Exit loop")
    option = input("Input your option: - ")#getting users option
    match option:#Checking what user chose
        case '1': add_new_member()#Add a newmmeber procedure
        case '2': display_all_mmebers()#Display list of all members procedure
        case '3': exit = True#Exit loop, by making exit, so killing while not exit condition.and
        case _: print("Input a valid option")#Error msg for invalid input
#Done in 29min 19.92s