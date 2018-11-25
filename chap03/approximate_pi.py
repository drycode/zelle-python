
import math
def main():
    n = eval(input("Enter how many terms: "))
    x = 0
    m = 1
    for i in range(1, 2 * n + 1, 2):
        x = x + (m * 4/i)
        m = -m
    print(math.pi - x)
main()
