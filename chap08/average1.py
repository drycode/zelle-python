def main():
    n = eval(input("How many numbers do you have? "))
    num = 0.0
    for i in range(n):
        x = eval(input("Enter a number >> "))
        sum = sum + x
    print("\nThe average of the numbers is", sum / n)

main()
