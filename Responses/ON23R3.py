import random; Temperatures = [[(round(random.uniform(15, 45),1)) for _ in range(24)] for _ in range(7)] #For making test data, not needed in 0478 syllabus.
Days = ['sunday','monday','tuesday','wednesday','thursday','friday','saterday']#Contain days of the week
#Finding the coldest and hottest temperatures, and the sum of all temperatures every day, and the average, also for the week
coldest = [(float("INF")) for _ in range(7)]; hottest = [(-float("INF")) for _ in range(7)]#For days
coldest_w = float('INF'); hottest_w = -float('INF')#For weeks
#to find average temperature of week, and per day
average = [0 for _ in range(7)]; total = [0 for _ in range(7)] #For days
average_w = 0;total_w = 0#For week
for day in range(7):
    for hour in range(24):
        if hottest[day] < Temperatures[day][hour]:hottest[day] = Temperatures[day][hour] #finding temperature of hottest temperature FOR day
        if coldest[day] > Temperatures[day][hour]:coldest[day] = Temperatures[day][hour]#Finding temperature with coldest temperature FOR day
        if coldest_w > Temperatures[day][hour]:coldest_w = Temperatures[day][hour]#finding temperature of coldest temperature FOR week
        if hottest_w < Temperatures[day][hour]:hottest_w = Temperatures[day][hour]#finding temperature of hottest temperature FOR week
        total[day] += Temperatures[day][hour] #Find total temperature
    average[day] = round(total[day] / 24, 1) #Finds average temperature for whole day
    total_w += total[day]
    print(f"For {Days[day]}, Minimum temperature was {coldest[day]}C and Maximum temperature was {hottest[day]}C. Average temperature was {average[day]}C")#Reporting data
average_w = round(total_w / (7*24), 1)#FInding average temp of week (24 hours a day, 7 days a week)
print(f"For the week, Minimum temperature was {coldest_w}C and Maximum temperature was {hottest_w}C. Average temperature was {average_w}C")#Reporting data