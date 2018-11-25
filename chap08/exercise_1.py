import math as m

def main():
    n = eval(input("What number in the Fibonnaci sequence would you like to see?: "))
    count = 0
    x = 1
    y = 0

    while count < n:
        count = count + 1
        z = x + y
        x = y
        y = z
    print(z)

main()
