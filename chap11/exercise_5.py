#(a) count(myList,  x)  (like myList.count(x))
def count(myList, x):
    tot = 0
    for i in myList:
        if i == x:
            tot = tot + 1
    return tot

#(b) isin(myList, x)    (like x in myList)
def isin(myList, x):
    for i in myList:
        if i == x:
            return True

#(c) index(myList, x)   (like myList.index(x))
def index(myList, x):
    for i in range (len(myList)):
        if myList[i] == x:
            return i
            break

#(d) reverse(myList)    (like myList.revers())
def reverse(myList):
    newList = []
    for i in range(len(myList)):
        x = myList[-1 * (i + 1)]
        newList.append(x)
    return newList

#(e) sort(myList)       (like myList.sort())
def sort(myList):
    newList = []
    for i in range (len(myList)):
        x = min(myList)
        newList.append(x)
        myList.remove(x)
    return newList

        


def main():
    myList = [8, 6, 7, 5, 3, 0, 9]
    myList = myList * 3
    x = 3
    print("Count of x: ", count(myList, x))
    print("X in myList: ", isin(myList, x))
    print("Index of x: ", index(myList, x))
    print("Reverse list: ", reverse(myList))
    print("Sort List: ", sort(myList))
if __name__ == '__main__': main()