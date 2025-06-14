MemberName = ["aal" for _ in range(200)]
MemberTime = [0 for _ in range(200)]
MemberCertificate = []
for member in range(200):#Input times for all members
    print(f"Hello {MemberName[member]}\nInput your time to complete the run")
    while True:#Verification check (Double entry)
        time1 = input("Input your time:- ")#Input once
        time2 = input("Input your time again: - ")#Input again
        try:
            if time1 == time2:#Compare, if same
                time1 = int(time1)#IF so, convert to integer
                print("Time accepted")
                break#Exit loop, go to next person
            else:##IF dont match
                print("Values muust match")#Error msg
        except ValueError:#If they input non-int value
            print("Input integer values")#Error msg
    MemberTime[member] = time1#Assign to memberTime list
#BUBBLE SORT
while True:#Repeat until swap is false (no swaps occur)
    swap = False#Set flag to false
    for element in range(200-1):#For each members data and stuff
        if MemberTime[element] > MemberTime[element+1]:#If prev ones larger then next one (illegal)
            MemberTime[element], MemberTime[element+1] = MemberTime[element+1], MemberTime[element]#kidnly tell them to swap
            MemberName[element], MemberName[element+1] = MemberName[element+1], MemberName[element]#Also make his complementry array swap, as theyre related (instructions said so)
            swap = True #A swap has occured, set flag to true
    if not swap: break #If no swaps have occured. exit loop
for member in range(200):#Repeat for each member
    if MemberTime < 240:#If members time is under 240s
        MemberCertificate.append(MemberName[member])#Put them in the list of the ppl who got certificates.
#Prints the list of winners
print(f"First place goes to {MemberName[0]}")#Prints who got first place
print(f"Second place goes to {MemberName[1]}")#Print who got 2nd place
print(f"Third place goes to {MemberName[2]}")#Print who got 3rd place