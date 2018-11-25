from random import random

def shuffle(myList):
    newList = []
    for i in range (len(myList)):
        x = int(random() * len(myList)) - 1
        newList.append(myList[x])
        myList.remove(myList[x])
    return newList

def main():
    myList = [8, 6, 7, 5, 3, 0, 9]
    myList = myList
    print("Shuffle List: ", shuffle(myList))

if __name__ == '__main__': main()