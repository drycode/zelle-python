def main():
    sum = 0.0
    #n = input("Enter a number (<Enter> to quit) >> ")
    n = 5
    while n > 0:
        x = n
        sum = x + sum
        n = n - 1

    print("\nThe sum of the numbers is", sum )
main()
