#One-dimensional random walk
from random import random

def main():
    printIntro()
    n = eval(input("How many steps do you intend to take per trip? "))
    avgTravel = avgSteps(n)
    print("The object will travel an average of", avgTravel, "based on the simulation.")

def printIntro():
    print("This program simulates a random walk in one dimension, where the")
    print("object will move either forward or backward at random. Varialble")
    print('"n" represents the number of random steps per trip. The program')
    print("will simulate 1000 trips by default, and will return the average")
    print("distance traveled per trip.")

def avgSteps(n):
    totTravel = 0
    for i in range (1000):
        steps = simNSteps(n)
        totTravel = totTravel + steps
    if totTravel == 0:
        avgTravel = 0
    else:
        avgTravel = totTravel / 1000
    return avgTravel

def simNSteps(n):
    steps = 0
    for i in range (n):
        x = 2 * random() - 1
        if x > 0:
            steps = steps + 1
        elif x < 0:
            steps = steps - 1
        else:
            steps = steps
    return steps

if __name__ == '__main__': main()
