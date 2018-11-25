#One-dimensional random walk
from random import random
import math as m

def main():
    printIntro()
    n = eval(input("How many steps do you intend to take per trip? "))
    avgDist = avgTravel(n)
    printSummary(avgDist)

def printIntro():
    print("This program simulates a random walk in two dimensions, where the")
    print("object will move either forward or backward, left of right at random.")
    print('Varialble "n" represents the number of random steps per trip. The program')
    print("will simulate 1000 trips by default, and will return the average")
    print("distance 'as the crow flies' traveled per trip.")

def avgTravel(n):
    totBlocks = 0
    avgDist = 0
    for i in range (1000):
        avgBlocks = simNBlocks(n)
        totBlocks = totBlocks + avgBlocks
    if totBlocks == 0:
        avgDist = 0
    else:
        avgDist = totBlocks / 1000
    return avgDist

def simNBlocks(n):
    blocksX = blocksY = 0
    for i in range (n):
        x = 4 * random()
        if 0 <= x < 1:
            blocksX = blocksX + 1
        elif 1 <= x < 2:
            blocksX = blocksX - 1
        elif 2 <= x < 3:
            blocksY = blocksY + 1
        else:
            blocksY = blocksY - 1

    avgBlocks = m.sqrt((blocksX ** 2 + blocksY ** 2))
    return avgBlocks

def printSummary(avgDist):
    print("The object will travel an average of {0:0.2f} blocks based on the simulation.".format(avgDist))

if __name__ == '__main__': main()
