def main():
    print("This program calculates the future value\n", "of a 10-year investment.")
    #principal = eval(input("Enter the initial principal: "))
    #apr = eval(input("Enter the annual interest rate: "))

    principal = 900
    apr = 5

    print("{0:<} {1:>10}".format("Year", "Value"))
    print("----------------")

    for i in range (10):
        principal = principal * (1 + .01 * apr)

        print("{0:>2}      ${1:<}.{2:0^2}".format(i+1, int(principal), int(principal%1 * 100)))

main()
