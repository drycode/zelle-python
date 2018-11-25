def main():
    print("This program calculates the future value\n", "of an investment compounded quarterly.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate in perecents: "))
    year = eval(input("Enter the length of investment in years: "))
    deposit = eval(input("Enter the amount to be deposited each month: "))

    for i in range (year * 4):
        principal = (principal * (1 + (apr/4 * .01))) + (deposit * 12)
    print("The value in", year, "years is", principal)

main()
