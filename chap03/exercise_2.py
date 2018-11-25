import math as m

def main():
    price, d = eval(input("Please enter the cost of the Pizza, and how big it was: "))
    A = m.pi * ((.5 * d) ** 2)
    price_sqin = price / A
    print("The price per square inch is", round(price_sqin, 2))

main()
