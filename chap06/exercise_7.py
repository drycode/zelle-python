import math as m
def fibonnaci(n):
    x = 0
    y = 1
    z = 0

    for i in range (n+1):
        z = x + y
        x = y
        y = z
    return y

def main():
    n = eval(input("What number in the Fibonnaci sequence would you like to see?: "))
    y = fibonnaci(n)
    print("The {0} Fibonnaci number is {1}.".format(n, y))
main()
