Customers = ["" for _ in range(100)] #names of customers
Quotations = [[0 for _ in range(5)] for _ in range(100)] #Oh fuck, stuff about customers (why so many)?
customer_count = 0
WoodType = [
    "Laminate",
    "Pine",
    "Oak"
]
Price = [
    29.99, #Laminate
    34.99, #Pine
    54.99  #Oak
]
#Getting and validating customers name and room datails
def get_customer_Details(customer_no:int):
    name = input("Input your name: - ")
    while True:
        try:
            length, width = map(float, input("Input the length and width of your room\n<in format 'LENGTH, WIDTH'. e.g. '4.5, 6.7'>\n: - ").split(',')); break #Get user input, leave
        except:
            print("!!!Invalid format. Pls reinput!!!")
    length, width = round(length, 1), round(width, 2) #Rounds both to 1.d.p
    if (length >= 1.5 and length <= 10) and (width >= 1.5 and width <= 10): #If both length and width are between 1.5 and 10.0 inclusive
        print("Length and width have been validated")
        return [length, width, name]
    else:
        print("Width and length are not withn required bounds.\n(between 1.5 and 10.0 INCLUSIVE)")
#Choose wood type
def wood_choice(roomarea, Types_of_wood, Prices_for_woods):
    print("here are the avalable wood types and their prices")
    for wood in range(len(Types_of_wood)):#NOTE lists types of woods avalable
        print(f"{wood+1}::{Types_of_wood[wood]} Costs ${Prices_for_woods[wood]}")
    while True:#NOTE: Validates the types of wood user wants to get
        option = int(input("Input the number of the wood you want\n:- "))
        if option >= 1 and option <= len(Types_of_wood):
            break
        else: print("Please reinput, as wood choice enterd is invalid")
    cost_of_wood = round(roomarea * Prices_for_woods[option-1], 2) #Calculates cost of wood
    #NOTE:Returns in the format  IN0: - The cost of the wood user wants to room area specs, IN2: - The option of wood user chose as an index
    return [cost_of_wood, option-1]
#Outputs quotation
def output_quotation(customers_name, choice_of_wood, calculated_price_of_chosen_wood_type):
    print(f"Details for customer {customers_name}")#Name of customr
    print(f"Customer chose wood type {WoodType[choice_of_wood]}")#wood type chosen
    print(f"Customer has to pay ${calculated_price_of_chosen_wood_type}") #Amount to pay
#Mainloop
while customer_count != 100:
    print("Welcome to wood floorings")
    room_details = get_customer_Details(customer_count)#Get room length and width
    room_area = round((room_details[0] * room_details[1]), 0) #Calculate area , rounds it to nearest whone number
    wood_details = wood_choice(room_area, WoodType, Price) #Get wood type, details and price
    #Assigns data to appropriate lists (very optomised)
    Customers[customer_count] = room_details[2];Quotations[customer_count][0] = room_details[0];Quotations[customer_count][1] = room_details[1];Quotations[customer_count][2] = room_area;Quotations[customer_count][2] = room_area;Quotations[customer_count][2] = room_area;Quotations[customer_count][3] = wood_details[1];Quotations[customer_count][4] = wood_details[0]
    #OUtputs data to user
    output_quotation(room_details[2], wood_details[1], wood_details[0])
    customer_count += 1 #Increment customer count