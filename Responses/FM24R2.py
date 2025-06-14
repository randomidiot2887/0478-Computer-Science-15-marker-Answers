StudentName = ['aiik', 'aaal', 'rodh', 'maaz']
ScreenTime = [[0 for _ in range(7)] for _ in range(4)]
ClassSize = 4
Total_Screen = [0 for _ in range(4)]
Days_With_Greater_then_300min_Screen = [0 for _ in range(ClassSize)]
least_weekly_mins = float('inf')
least_weekly_mins_student = ""
total_screen = 0
for student in range(ClassSize):#Lopps for each student
    print(f"Hey {StudentName[student]}! Lets enter your screen time in minutes for")
    for day in range(7):#Loops for each day
        ScreenTime[student][day] = int(input(f"Day {day}: - "))#Inputting number of minutes spent as screentime
        Total_Screen[student] += ScreenTime[student][day] #totaling screentime muny=utes per week
        if ScreenTime[student][day] > 300:#Finds and counts days with more then 300 min screentime
            Days_With_Greater_then_300min_Screen[student] += 1
    if least_weekly_mins > Total_Screen[student]:#FInds student with least screentime
        least_weekly_mins = Total_Screen[student]
        least_weekly_mins_student = StudentName[student]#Find their name
    total_screen += Total_Screen[student]
    print(f"Student {StudentName[student]} spent a total of {Total_Screen[student]//60} hours and {Total_Screen[student] - ((Total_Screen[student] // 60)*60)} minutes on screen during the week. and student has spent {Days_With_Greater_then_300min_Screen[student]} days with over 300 minutes of screen")
print(f"Student with least screentime is {least_weekly_mins_student}! Congrats. just dont get hooked on insta!")
av_screen_tm = total_screen // ClassSize
print(f"Average screentime weekly for class is {av_screen_tm} minutes")