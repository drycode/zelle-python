#Syracuse sequence
def syr(x):
    if x % 2 == 0:
        syrX = x/2
    elif x % 2 == 1:
        syrX = 3 * x + 1
    return syrX

def main():
    x = eval(input("Input a natural number: "))
    print(x)
    while x > 1:
        syrX = syr(x)
        x = syrX
        print(syrX)
main()
