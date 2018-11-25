#2, 3, or 12 the player loses
#7 or 11 the player wins
#Any other roll initiates roll for points
    #Roll for 7 (loss) or 11 (win)
from random import randrange

def main():
    printIntro()
    n = eval(input("How many rolls should I simulate? >> "))
    wins, losses = simNCraps(n)
    printSummary(wins, losses, n)

def printIntro():
    print("This program is designed to simulate (n) games of craps")
    print("and will return the probability of winning based on the")
    print("simulation.")

def simNCraps(n):
    wins = 0
    losses = 0
    for i in range(n):
        if simOneCraps() is True:
            wins = wins + 1
        else:
            losses = losses + 1
    return wins, losses


def simOneCraps():
    x = randrange(2,12)
    if x == 2 or x == 3 or x == 12:
        return False
    elif x == 7 or x == 11:
        return True
    else:
        y = 0
        while x != y and x != 7:
            y = randrange(2, 12)
            if y == 7:
                return False
            elif y == x:
                return True

def printSummary(wins, losses, n):
    print("\nGames simulated: ", n)
    print("Winning rolls: {0} ({1:0.1%})".format(wins, wins/n))
    print("Losing rolls: {0} ({1:0.1%})".format(losses, losses/n))


if __name__ == '__main__': main()
