def main():
    n = eval(input("How many numbers would you like to add? "))
    x = eval(input(": "))
    for factor in range (2, n+1):
        y = eval(input(": "))
        x = x + y
    print("Your final sum is: ", x)

main()
