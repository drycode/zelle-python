
def palindrome(xStr, firstRun=True):
    if firstRun == True:
        for ch in '<}{ ][>.?/:;\|+=-_),(*&^%$#@!~`':
            xStr.replace(ch, "")
        xStr = xStr.lower()
    
    if len(xStr) < 2:
        return True
    elif xStr[0] == xStr[-1]:
        xStr = xStr[1:-1]
        palindrome(xStr, firstRun=False)
        return True
    else:
        return False
        
def main():
    xStr = input("Type a phrase to check for palindrome status....")
    if palindrome(xStr) is True:
        print("The phrase is a palindrome.")
    else:
        print("The phrase is not a palindrome.")
main()
    

