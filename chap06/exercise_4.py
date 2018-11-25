def sumN(n):
    fact = 1
    for factor in range(n,1,-1):
        fact = fact + factor
    return fact
def sumNCubes(n):
    cube = 1
    for factor in range(n,1,-1):
        cube = cube + factor ** 3
    return cube
def main():
    n = eval(input("Enter a value: "))
    N = sumN(n)
    NCubes = sumNCubes(n)
    print("The sum of the first {0} natural numbers is {1}, and the sum of the\n"
    "sum of the first {0} cubes is {2}".format(n, N, NCubes))

main()
