def toNumbers(strList):
    for x in range (len(strList)):
        strList[x] = int(strList[x])
    return(strList)
def test():
    list = ['1','2','3','4','5']
    z = toNumbers(list)
    print(z)
test()
