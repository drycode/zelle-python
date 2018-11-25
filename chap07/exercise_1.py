def main():
    x = 0
    while x <= 0:
        try:
            x, y = eval(input("How many hours worked, and how much per hour? "))
        except NameError:
            print("Make sure to enter 2 numbers, separated by a comma")
        except TypeError:
            print("Make sure to enter 2 numbers, separated by a comma")
        except SyntaxError:
            print("Make sure to enter 2 numbers, separated by a comma")

    if x <= 40:
        pay = x * y
    else:
        pay = 40 * y
        pay = (x - 40) * 1.5 * y + pay
    print(pay)

main()
