def main():
    #Get name from user and store as a string
    name = input("What is your name? \n")

    #Convert to all lower
    name = name.lower()

    #Convert to numbers, subtract 96 from each, and accumulate
    x = 0
    for ch in name:
        x = int(ord(ch)) + x - 96

    print("The numeric value of your name is {0}.".format(x))

main()
