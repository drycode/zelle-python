#if year is divisible by 4, it's a leap years
#unless it's a century year not divisible by 400
#leap year yes or no

def leapYear(year):
    if (year %4) != 0:
        print("{} is not a leap year.".format(year))
    else:
        if (year % 100) == 0:
            if (year % 400) ==0:
                print("{} is a leap year.".format(year))
            else:
                print("{} is not a leap year.".format(year))
        else:
            print("{} is a leap year.".format(year))


def main():
    year = 1900
    leapYear(year)
main()
