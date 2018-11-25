def main():
    x1, y1 = eval(input("Enter the first point values of x,y: "))
    x2, y2 = eval(input("Enter the second point values of x,y: "))
    slope = (y2 - y1) / (x2  - x1)
    print("The slope of the line is", slope)
main()
