import math as m
def main():
    x1, y1 = eval(input("Enter the first point values of x,y: "))
    x2, y2 = eval(input("Enter the second point values of x,y: "))
    distance = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance between these two points is", distance)

main()
