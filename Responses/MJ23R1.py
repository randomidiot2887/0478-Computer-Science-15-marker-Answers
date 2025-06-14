Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saterday'] #Days of the week
Readings = [[0 for _ in range(24)] for _ in range(7)] #Store 24 readings per day for 7 days
AverageTemp = [0 for _ in range(7)] #Store average temperature for each day of the week
#Max and Min temps
MaxTemp = +50.0
MinTemp = -20.0

def CtoF(celcius): #Convert celcius to farenhite
    farenhite = (celcius * 9/5 + 32)
    return farenhite

#Input and validate hourly temps for one week
TotalTemp_PerWeek = 0
for day in range(7):
    TotalTemp_PerDay = 0
    print(f'For {Days[day]}, input hourly temperatures for each hour\nIn degreese celcius:')
    for hour in range(24):
        while True:
            HourlyTemp = int(input(f"For {hour+1}00 Hours: - "))
            if HourlyTemp >= MinTemp and HourlyTemp <= MaxTemp: #If temperature withn valid bounds
                Readings[day][hour] = HourlyTemp
                TotalTemp_PerDay += Readings[day][hour] #Totals temperature per day for calculating average
                print(f"Temperature input succesfully for {hour+1}00 Hours")
                break #Exit loop
            else:#Give error message if not withn bounds
                print(f"Temperature must fall between {MinTemp} degreese celcius and {MaxTemp} degreese celcius. \nPlease reinput temperature")
    print(f"Temperatures succesfully enterd for {Days[day]}")
    AverageTemp[day] = TotalTemp_PerDay / 24 #Finds temperature average for whole day
    TotalTemp_PerWeek += AverageTemp[day] #Finds total for whole week
    print(f"Average Temperature for {Days[day]} is\n{AverageTemp[day]} degreese Celcius\n{CtoF(AverageTemp[day])} degreese Farenhite\n")#Display average temp for each day in C and F

AverageTemp_ForWeek = TotalTemp_PerWeek / 7
print(f"Average temperature for whole week is\n{AverageTemp_ForWeek} degreese Celcius\n{CtoF(AverageTemp_ForWeek)} degreese Farenhite")#Display average temp for whole week in C and F
 

