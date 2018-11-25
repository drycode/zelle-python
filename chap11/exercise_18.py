#One-dimensional random walk (log blocks traveled)
from random import random

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

def printIntro():
    print("This program simulates a random walk in one dimension, where the")
    print("object will move either forward or backward at random. Variable")
    print('"n" represents the number squares on the block. The program')
    print("will return how many times each square is stepped on.")

def main():
    printIntro()
    n = eval(input("How many squares are on the sidewalk?"))
    squares = []
    for i in range(n + 1):
        squares.append(0)
    
    steps = int(n / 2)
    while 0 < steps < n:
        x = 2 * random() - 1
        if x > 0:
            steps = steps + 1
            squares[steps] = squares[steps] + 1
        elif x < 0:
            steps = steps - 1
            squares[steps] = squares[steps] + 1
        else:
            steps = steps
    for i in range(len(squares)):
        print("Square {0}: {1}".format(i + 1,squares[i]))

if __name__ == '__main__': main()

