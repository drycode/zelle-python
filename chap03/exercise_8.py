import math as m

def main():
    year = eval(input("Input the 4 digit year"))
    C = year // 100
    epact = (8 + (C//4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30
    print("the Gregorian Epact value is", epact)

main()
