Contacts = [['' for _ in range(2)] for _ in range(100)]
CurruntSize = 0
#DIsplay menu of choices, and validates input
def menu():
    while True:#Repeats until valid input has been input
        print("Menu of choices")
        print("1 : Enter new contacts")
        print("2 : Display new contacts")
        print("3 : Delete all the contacts")
        option = input("Input your option (1, 2 or 3)\n: - ")#Get user input
        if option == '1' or option == '2' or option == '3':#IF its either 1, 2 or 3
            return int(option)#Return it, to the rest of the program
        else:#IF not 1, 2 or 3
            print("Invalid option. Please reenter your option")#Display error msg
#Menu to add a new contact to it
def new_contact(number_of_stored_contacts):
    while True:
        print("Welcome to ADD mew contacts")
        num_new_contacts = int(input("How many contacts will you add (Max 5)\n: - "))#Inputting the number of contacts to add
        if num_new_contacts >= 1 and num_new_contacts <= 5:#If its in the valid max 5 range
            for _ in range(num_new_contacts):#Repeating for each new contact to be added
                contact_name = input("Input contact name: - ")#Input contacts name
                contact_phone_no = input("Input contacts phone number: - ")#Input contacts phone number
            break#Exits the while loop, validated
        else:#If not in the range
            print("A maximum of 5 contacts can be added at once")#The value not in range of 5, or is 0
    for contact in range(100):#Repeats for each contact in the array
        if Contacts[contact][0] == "":#If the position is empty
            Contacts[contact][0] = contact_name#Add the contact name
            Contacts[contact][1] = contact_phone_no#Add contact phone no
            number_of_stored_contacts += 1#Increment currunt size
            break
    return number_of_stored_contacts
def display_contacts():#Displays all the contacts
    for contact in range(100):#Repeats for each contact in Contacts[]
        if Contacts[contact][0] != '':#If contact not empty
            print(f"Name: - {Contacts[contact][0]} PhoneNo: - {Contacts[contact][1]}")#Display details

def delete_contacts():#Deletes all contacts
    for Contact in range(100):#For every contact
        Contacts[Contact][0], Contact[Contact][1] = "", ""#Set all of it to zero
    print("Contacts have been deleted")

while True:
    match menu():#Get and do appropriate action
        case 1:CurruntSize = new_contact(CurruntSize)#Add new contact
        case 2:display_contacts()#Diaplay all contacts
        case 3:delete_contacts()#Delete all contacts
