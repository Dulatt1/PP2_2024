# программа которая выводит прошлую и будущую дату по дням

import datetime

y, m, d = [int(x) for x in input("Enter date (year, month, day): ").split()]
n = int(input("Days: "))
currentDate = datetime.date(y, m, d)
pastDate = currentDate - datetime.timedelta(days = n)
futureDate = currentDate + datetime.timedelta(days = n)
print("Past date: ", pastDate)
print("Future date: ", futureDate)


