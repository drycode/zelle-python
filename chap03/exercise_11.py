#Sum of the first n natural numbers
def main():
    n = eval(input("What is the value of n? "))
    sum = 1
    for factor in range (2, n+1):
        sum = sum + factor
    print("The sum of of the first", n, "natural numbers is", sum)

main()
