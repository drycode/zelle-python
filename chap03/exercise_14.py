def main():
    n = eval(input("How many numbers would you like to average? "))
    x = eval(input(": "))
    for factor in range (2, n+1):
        y = eval(input(": "))
        x = float(x) + float(y)
    print("Your final average is: ", x / n)

main()
