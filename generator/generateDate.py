##
# @author Yamao Cuzou <yamao.cuzou@ynov.com>
 # @file Description
 # @desc Created on 2023-10-23 8:32:40 pm
 # @copyright Cuzou Corporation
 #

import random

def generate_random_date(isHireDate):
    date = ""
    day = random.randint(1500, 3000) % 31
    month = random.randint(1500, 3000) % 12
    date += str(day) + "/" if day >= 10 else "0" + str(day) + "/"
    date += str(month) + "/" if month >= 10 else "0" + str(month) + "/"
    if (isHireDate == False):
        date += str(random.randint(1940, 2005))
    else:
        date += str(random.randint(1995, 2005))
    return date

dateList = [generate_random_date(False) for _ in range(1000)]

with open("csv/birthDates.csv", "w") as file:
    file.write("BirthDate\n")
    for date in dateList:
        file.write(f"{date}\n")
file.close()


dateList = [generate_random_date(True) for _ in range(1000)]

with open("csv/hireDates.csv", "w") as file:
    file.write("HireDate\n")
    for date in dateList:
        file.write(f"{date}\n")
file.close()