import math as m
def main():
    a, b, c = eval(input("Input the 3 sides of the triangle, separated by commas: "))
    s = (a + b + c) / 2
    A = m.sqrt(s * (s-a) * (s-b) * (s-c))
    print("The area of this triangle is: ", round(A, 2))

main()
