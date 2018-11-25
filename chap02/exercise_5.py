def main():
    print("This program calculates the future value\n", "of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate in perecents: "))
    year = eval(input("Enter the length of investment in years: "))

    for i in range (year):
        principal = principal * (1 + (apr * .01))
    print("The value in", year, "years is", principal)

main()
