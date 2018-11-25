import math

def main():
    print("Given radius, this program will calculate the volume and\n","surface area of a sphere")
    r = (eval(input("Input a value for the radius: ")))
    V = 4/3 * math.pi * (r ** 3)
    A = 4 * math.pi * (r*r)
    print("A sphere with radius", r, "has volume", round(V, 3), "and surface area", round(A, 3),".")

main()
