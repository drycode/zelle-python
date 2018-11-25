import math as m
def main():
    height, angle = eval(input("What is the height of the house in ft, and the angle of the ladder in degrees? "))
    length = height / (m.sin((m.pi / 180 * angle)))
    print("The ladder must be", round(length, 2), "ft in length")

main()
