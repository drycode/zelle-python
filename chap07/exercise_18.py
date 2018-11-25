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

def main():
    try:
        dateStr = input("Please enter a date in form 00/00/0000: ")

        monthStr, dayStr, yearStr = dateStr.split("/")
        month = int(monthStr)
        day = int(dayStr)
        year = int(yearStr)
    
        
        if month > 12 or day > 31:
            print("This date is invalid.")
        else:
            if day <= 28:
                print("This date is valid.")
            elif month == 2 and day == 29:
                if leapYear(year) == False:
                    print("This date is invalid.")
                else:
                    print("This date is valid.")
            elif day == 31:
                if month == 2 or 4 or 6 or 11:
                    print("This date is invalid")
                else:
                    print("This date is valid")
            else:
                print("The date is valid.")

    except ValueError:
        print("Your input was not in the correct form.")
    except:
        print("Oops. Something went wrong!")
main()
