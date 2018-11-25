from cube import Cube

def main():
    side = eval(input("What is the side length of your cube?  "))
    cube = Cube(side)
    A = cube.surfaceArea()
    V = cube.volume()
    print("The volume of your cube is {0:0.1f}.".format(V))
    print("The area of your cube is {0:0.1f}.".format(A))
main()
