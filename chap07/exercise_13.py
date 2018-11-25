#accepts date
#verifies it
#calculates day number
def leapYear(year):
    if (year % 4) != 0:
        return False
    else:
        if (year % 100) == 0:
            if (year % 400) ==0:
                return True
            else:
                return False
        else:
            return True

def verDate(month, day, year):
    if month > 12 or day > 31:
        return False
    else:
        if day <= 28:
            return True
        elif month == 2 and day == 29:
            if leapYear(year) == False:
                return False
            else:
                return True
        elif day == 31:
            if month == 2 or 4 or 6 or 11:
                return False
            else:
                return True
        else:
            return True
def main():
    dateStr = '05/25/1885'

    monthStr, dayStr, yearStr = dateStr.split("/")
    month = int(monthStr)
    day = int(dayStr)
    year = int(yearStr)

    if verDate(month, day, year) == False:
        print("This date is invalid.")
    else:
        dayNum = 31 * (month - 1) + day
        if month == 2:
            if leapYear(year) == True:
                dayNum = dayNum - (4 * (month) + 23)//10 + 1
            else:
                dayNum = dayNum - (4 * (month) + 23)//10
        else:
            dayNum = 31 * (month - 1) + day
    print("The numeric value of this date is {}.".format(dayNum))
main()
