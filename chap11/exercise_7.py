def main():
    myList = [8,6,7,5,3,0,9]
    newList = [9,0,3,5,7,6,8]

    sum = 0
    for i in range(len(myList)):
        x = myList[i] * newList[i]
        sum = sum + x
    print(sum)
main()