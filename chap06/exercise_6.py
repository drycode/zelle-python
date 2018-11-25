import math as m
def triangle(a, b, c):
    s = (a + b + c) / 2
    A = m.sqrt(s * (s-a) * (s-b) * (s-c))
    return A

def main():
    a, b, c = eval(input("Input the 3 sides of the triangle, separated by commas: "))
    A = triangle(a, b, c)
    print("The area of this triangle is: ", round(A, 2))
main()
