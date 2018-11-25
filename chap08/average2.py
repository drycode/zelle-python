#Interactive Loop
def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >> "))
        sum = sum + x
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", sum / count)

main()
