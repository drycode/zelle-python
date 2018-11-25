import math as m
def pizzArea(diameter):
    area = m.pi * ((.5 * diameter) ** 2)
    return area
def pizzPrice(cost, area):
    price_sqin = cost / area
    return price_sqin
def main():
    price, d = eval(input("Please enter the cost of the Pizza, and how big it was: "))
    A = pizzArea(d)
    price_sqin = pizzPrice(price, A)
    print("The pizza has an area of {0} square inches".format(round(A, 2)))
    print("The price per square inch is about ${0}.".format(round(price_sqin, 2)))

main()
