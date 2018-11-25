def Easter(year):
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        if (d + e) > 9:
            if year == 1954 or 1981 or 2049 or 2076:
                d = d - 7
                print("Easter falls on April {}.".format(d + e - 9))
            else:
                print("Easter falls on April {}.".format(d + e - 9))
        else:
            if year == 1954 or 1981 or 2049 or 2076:
                d = d - 7
                print("Easter falls on March {}.".format(22 + d + e))
            else:
                print("Easter falls on March {}.".format(22 + d + e))
    else:
        print("Year is out of range")


def main():
    #year = eval(input("Input a year: "))
    year = 2049
    Easter(year)
main()

#1954, 1981, 2049, 2076 one week too late
