import math as m
def main():
    n = eval(input("What number in the Fibonnaci sequence would you like to see?: "))
    x = 1
    y = 0

    for i in range (n+1):
        z = x + y
        x = y
        y = z
        print(i, ":", y)
main()
