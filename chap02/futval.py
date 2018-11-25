def main():
    print("This program calculates the future value\n", "of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range (10):
        principal = principal * (1 + apr)

    print("The value in 10 years is:", principal)
    
main()
