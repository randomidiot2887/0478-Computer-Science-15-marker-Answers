Account = [
    ['aid', 'aal', 'roodh'], #Usernames
    ['aidiscool69', 'Aal*I$C001', 'roodhroodh'] #Passwords
]
ACCDetails = [
    [3940, 5, 982],#balance
    [89, 34, 834],#Overdraft Limit
    [807, 100, 983]#Withdrawal Limit
]

Size = 3 #3 Accounts

def disp_Balance(UserID):
    print(f"Balance ramining for user {Account[0][UserID]} is ${ACCDetails[0][UserID]}") #Displays balance

def withdraw_Money(UserID):#Withdraw money
    print("Enter the amount of money you`d like to withdraw")
    while True:
        amountMoney_Withdrawn = float(input("Withdrawal ammount : - "))
        if (ACCDetails[0][UserID] - amountMoney_Withdrawn) >= (-ACCDetails[1][UserID]):#Overdraft limit check
            print("Passed overdraft limit check")
            if amountMoney_Withdrawn <= ACCDetails[2][UserID]:#Withdrawal limit check
                print("Passed withdrawal limit check.\nWithdrawal succesfull")
                ACCDetails[0][UserID] -= amountMoney_Withdrawn#Do the operation
                break
            else:print("Failed withdrawal limit check. Withdrawal failed\n[You withdrew too much at once].\nInput a amount to withdraw thats less then your withdrwal limit")
        else:print("Failed overdraft limit check.\n[You are trying to withdraw an amount that would reduce the amount of cash in your account below withdrawal limit]\nInput a value less then that")

def deposit_money(UserID):
    AMount_DePosIt = float(input("Input the amount of money to deposit in your account\n: - $"))#Amount to deposit
    ACCDetails[0][UserID] += AMount_DePosIt#Depositing more money
    print(f"Deposit succesful. You have a total of ${ACCDetails[0][UserID]}")

#Get yser login details
print("Welcome to Cambridge International Banking.\nThis is bank NO MV609.\nPlease login to see our amazing services here")

while True:
    flag = False#Authunticated
    username = input("Input Username: - ")
    password = input("Input Password: - ")
    for profile in range(len(Account[0])):#Checm if username exists and if password is correct
        if Account[0][profile] == username and Account[1][profile] == password:
            profile_ID = profile #Assigns index of users profile (Account)
            print("User login has been validated")
            flag = True
            break
        else: print("Username or Password is incorrect. Please retry.")
    if flag:
        break
while True:#MAIN MENU
    print("Welcome to the main menu.")
    print("Options")
    print("------------")
    print("1:DISPLAY BALANCE\n2:WITHDRAW MONEY\n3:DEPOSIT MONEY\n4:EXIT")
    option = input("Input OPTION: - ")
    match option:#VALIDATING AND PERFORMING APPROPRIATE OPTION
        case '1':disp_Balance(profile_ID)
        case '2':withdraw_Money(profile_ID)
        case '3':deposit_money(profile_ID)
        case '4':print("Exiting");break#EXITING
        case _:print("INVALID OPTION. PLS REINPUT")