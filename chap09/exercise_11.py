from random import randrange

def main():
    printIntro()
    n = eval(input("Simulations: "))
    totFive = simNRolls(n)

def printIntro():
    print("This program is intended to simulate the rolling of five six-sided")
    print("dice to approximate the probability of rolling five-of-a-kind.")

def simNRolls(n):
    totFive = 0
    for i in range (n):
        if not fiveOfAKind():
            totFive = totFive
        else:
            totFive = totFive + 1
    return totFive

def fiveOfAKind():
    a, b, c, d, e = simOneRoll()
    if a == b == c == d == e:
        return True
    else:
        return False

def simOneRoll():
    dice = []
    for i in range (5):
        x = randrange(1, 6)
        dice.append(x)
    return dice

if __name__ == '__main__': main()
