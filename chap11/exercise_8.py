#can also use "x in myList"
def isin(myList, x):
    for i in myList:
        if i == x:
            return True

def removeDuplicates(myList):
    newList = []
    for i in myList:
        if not isin(newList, i):
            newList.append(i)
    return newList

def main():
    myList = [8, 6, 7, 5, 3, 0, 9]
    myList = myList * 3
    print("Remove Duplicate: ", removeDuplicates(myList))

if __name__ == '__main__': main()