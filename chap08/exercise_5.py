#Prime number validation
#This program will close if the number is not prime,
#and will report an error if the input is invalid

import math as m

def main():
    #n = eval(input("Input a positive whole number: "))
    n = 25
    while (n < 1) or (n % 1 != 0):
        n = eval(input("Try a positive whole number: "))


    for i in range (int(m.sqrt(n))):
        i = 2
        if (n % (i)) != 0:
            i = i+1
            if i > m.sqrt(n):
                exit()
        else:
            break
    print("The number is prime.")
main()
