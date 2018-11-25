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
    x = 0
    #Validate x as a positive whole number
    while True:
        x = eval(input("Input a positive whole number: "))

        if (x % 1 != 0):
            x = print("The number you entered was not whole!")
        elif (x < 1):
            x = print("The number you entered was not positive!")
        else:
            break
    for n in range(x):
        primeNum(n+1)

main()
