#Sum of the cubes of the first n natural numbers
def main():
    n = eval(input("What is the value of n? "))
    cube = 1
    for factor in range (2, n+1):
        cube = cube + factor ** 3
    print("The cube of the first", n, "natural numbers is", cube)

main()
