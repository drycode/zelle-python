from sphere import Sphere

def main():
    r = eval(input("What is the radius of your sphere?  "))
    s = Sphere(r)
    A = s.surfaceArea()
    V = s.volume()
    print("The volume of your sphere is {0:0.1f}.".format(V))
    print("The area of your sphere is {0:0.1f}.".format(A))
main()
