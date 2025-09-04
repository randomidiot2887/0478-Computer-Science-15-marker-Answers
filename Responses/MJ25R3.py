records = 10000                                                         # Make data structures (lists) hold max 10000 video's info
Video = [['' for _ in range(4)] for _ in range(records)]                # Data structure that stores video details
Results = ['' for _ in range(records)]                                  # Data structure that stores search results
def menu():                                                             # Defining the menu function, which displays the main menu the user interacts with and validates input
    print('Main Menu')  
    print('----------------')
    print('1: Add new video')
    print('2: Search video')
    print('3: Exit')
    print('----------------')                # Set flags to False
    while True: 
        option = int(input('Input your desired option: - '))            # Gets user input, convert it to integer
        add_new, search, exit_program = False, False, False             # Sets flags to False                                            
        match option:                                                   # Uses case to check value of option
            case 1:                                                     # If option = 1
                print('Entry Succesful')                                # Prints that entry is succesful
                add_new = True                                          # Sets flag to True
            case 2:                                                     # If option = 2
                search = True                                           # Sets flag to True
            case 3:                                                     # If option = 3
                exit_program = True                                     # Sets flag to True
            case _:                                                     # else 
                print('Invalid option entered.')                        # Informs user their choice is wrong
        return_value = [add_new, search, exit_program]                  # Sets up the data structure to be returned
        if return_value != [False, False, False]:                       # Check if the choice is valid
            return return_value                                         # Returns the value

def search_engine(title, video, record):
    """
    Handles the actrual searching through the video list for the video
    This uses linier search to find the titles that match and stuff those records into temp results
    then if its found, return the results. else return -1, an error code
    """
    temp_results = [['' for _ in range(4)] for _ in range(record)]
    found = False
    for id in range(record):
        if video[id][0] == title:
            temp_results[id] = video[id]
            found = True
    if not found:
        return -1
    else:
        return temp_results

def new_vid_entry(records, video):
    '''
    Handles the entry of new video's details
    first gets the values, then it asks user for input of another video
    if invalid option, it lets user know and prompts for input
    and, once user input sucess, it puts those values in the videoes list
    '''
    Exit = False
    print('Input details for video')
    while not Exit:
        title = input('Title: ')
        Format = input('Format: ')
        year = input('Year of release: ')
        SCode = input('Storage code: ')
        temp = input("Do you want to add another video's details? (y/n): ").lower()
        while True:
            if temp == 'n':
                Exit = True
                break
            elif temp == 'y':
                print('Input details for next video')
                break
            else:
                temp = input("Invalid option -> ('y' = yes, 'n' = no):.")
        
        for element in range(records):
            if video[element] == ['', '', '', '']:
                video[element] = [title, Format, year, SCode]
                break
    return video
def search():
    '''
    Handles the user facing part of the search function,
    if found, it primts video onfo of matching title
    else, it prints the error message that no error is found
    '''
    found = False
    Title = input('Input the title of the video you want to find\n(E.g. Harry Potter and the Philosophers Stone):. ')
    temp = search_engine(Title, Video, records) 
    if temp != -1:
        found = True
        Results = temp
    else:
        print('Video not found')
    
    if found:
        for result in Results:
            if result != ['', '', '', '']:
                print('------------------------------')
                print(f'Title: {result[0]}')
                print(f'Format: {result[1]}')
                print(f'Year: {result[2]}')
                print(f'Storage Code: {result[3]}')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

def main():
    while True:                                     # Repeats until break'ed
        option = menu()                             # Shows user main menu and gets user input
        if option == [True, False, False]:          # If the returned value is corrosponding to new video entry
            new_vid_entry(records, Video)           # Call the procedure for entring new video details and storing them
        elif option == [False, True, False]:        # if the returned value is corrosponding to search
            search()                                # call the search part
        elif option == [False, False, True]:        # If user wants to exit
            break                                   # Exits the program

if __name__ == '__main__':                          # If the program is running not imported
    main()                                          # Run the main function


# Alternatively, you can just call main()