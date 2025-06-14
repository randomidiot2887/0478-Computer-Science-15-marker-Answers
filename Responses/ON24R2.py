Rooms = ["" for _ in range(20)]
Dimensions = [[0 for _ in range(3)] for _ in range(20)]
Number = 0

while True:#Repeats until the number of rooms are valid
    Number = int(input("Input the number of rooms in your house: - "))#Gets input
    if Number >= 3 and Number <= 20:#IF between 3 and 20 inclusive
        print("Accepted"); break#Accept, and leave
    elif Number < 3:#If less then 3
        print("Denied, less then 3 rooms is forbidden")#Deny, error msg
    elif Number > 20:#If greater then 20
        print("Denied, more then 20 rooms is forbidden")#Deny error msg 2
largest_room = ""#Initialising variable,m to store largest rooms name in
largest_room_area = -float("inf")#Store the area of largest riin
smallest_room = ""
smallest_room_area = float("inf")
TotalArea = 0
for room in range(Number): #Repeats for each room
    Rooms[room] = input(f"Input the name of room {room}: - ")#Gets the name of a room
    Dimensions[room][0] = int(input("Input the length of room: - "))#Gets length of room
    Dimensions[room][1] = int(input("Input the width of room: - "))#Gets width of room
    Dimensions[room][2] = round(Dimensions[room][0] * Dimensions[room][1], 2)#Calculate area of room, to 2.d.p
    TotalArea += Dimensions[room][2]#Totals area, to find average later on
    if largest_room_area < Dimensions[room][2]:#Checks if its largest area room
        largest_room_area = Dimensions[room][2]#IF so, store area
        largest_room = Rooms[room]#Store room area
    if smallest_room_area < Dimensions[room][2]:#Checks if its shallest area room
        smallest_room_area = Dimensions[room][2]#IF so, store area
        smallest_room = Rooms[room]#Store room area
    print(f"{Rooms[room]} has length {Dimensions[room][0]}m and has width {Dimensions[room][1]}m and has area of {Dimensions[room][2]}m^2")
print(f"Largest room is {largest_room}")
print(f"Smallest room is {smallest_room}")
print(f"Total area of house is {TotalArea}m^2 and average room area is {round(TotalArea/Number , 2)}m^3")
