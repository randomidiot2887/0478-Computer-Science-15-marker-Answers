PickerName = ["Zebra" for _ in range(3)]
PickedWeight = [0 for _ in range(3)]
no_mmebers = len(PickerName)
PickerCertificate = []
no_certs = 0
#Input weight of pick
for member in range(no_mmebers): #For eacg member
    print(f"Hey {PickerName[member]}, input the weight of your pick in killograms to 1 decimal place.\ne.g: 9.2kg (without unit, so 9.2  Otherwise program will 110% crash)")#Greet + Instructions
    PickedWeight[member] = round(float(input(": - ")), 1)#Ask to input pickedweight
    if PickedWeight[member] > 3: #If ersons pick is greater then 3kg
        PickerCertificate.append(PickerName[member])#Adds them to list if ppl who get certs
        no_certs += 1#Incrememnt the number of certs to be printed
#Sort lists in decending order of PickedWright[]
while True:
    swap = False#sets flaag to false
    for element in range(no_mmebers-1):#Repeats for each member-1
        if PickedWeight[element] < PickedWeight[element+1]:#Compares values
            PickedWeight[element], PickedWeight[element+1] = PickedWeight[element+1], PickedWeight[element] #Swap picked weight
            PickerName[element], PickerName[element+1] = PickerName[element+1], PickerName[element]#Swap picker names
            swap = True #Sets swap flag to true 
    if not swap:#If no swaps have occured
        break#Exit the loop
    #Display requird info
print(f"{PickerName[0]} is Best in Group")#Output best person
print(f"{PickerName[1]} is Second Best in Group")#Output 2nd best person
print(f"{no_certs} certificates need to be printed")#Output number of certs to be printed
