#This program validates input n as a prime number. The program will close
#if it finds n to be divisible by any number other than 1 and itself.

import math as m
#Validate n as a positive whole number
def main():
    n = eval(input("Input a positive whole number: "))
    
    if n == 0:
        n = eval(input("Your number must be higher than 0: "))
    elif (n % 1 != 0):
        n = eval(input("The number you entered was not whole: "))
    elif (n < 1):
        n = eval(input("The number you entered was not positive: "))
    else:
        #check if n is evenly divisible by values between 2 and int(m.sqrt(n))
        x = m.sqrt(n)
        i = 2


        while i <= x:
            value = n % i
            #if any value is divisble, break and close program
            if value == 0:
                exit()
            #if no value is divisible evenly, print("The number is prime.")
            else:
                i = i + 1
        print("The number is prime.")

main()
