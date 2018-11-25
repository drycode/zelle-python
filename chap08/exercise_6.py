#This program finds every prime number less than or equal to input n

import math as m

def primeNum(n):

        #check if n is evenly divisible by values between 2 and int(m.sqrt(n))
        x = m.sqrt(n)
        i = 2

        while i <= x:
            value = n % i
            #if any value is divisble, break and close program
            if value == 0:
                return
            #if no value is divisible evenly, print("The number is prime.")
            else:
                i = i + 1
        print(n)

def main():
    x = eval(input("Input a positive whole number: "))
    #Validate x as a positive whole number
    if x == 0:
        x = eval(input("Your number must be higher than 0: "))
    elif (x % 1 != 0):
        x = eval(input("The number you entered was not whole: "))
    elif (x < 1):
        x = eval(input("The number you entered was not positive: "))
    else:
        for n in range(x):
            primeNum(n+1)

main()
