import math as m

def main():
    x = eval(input("Enter a value: "))
    y = eval(input("How many iterations of Newton's formula would you like?: "))

    g = x / 2

    for i in range (y):
        g = (g + x / g) / 2
    print(g, ":", (g - m.sqrt(x)))
main()
        
