from random import randrange

def main():
     printIntro()
     n = eval(input("Iterations: "))
     for i in range (13):
        i = i + 1
        busts = simNHands(n, i)
        printSummary(busts, n, i)

def printIntro():
    print("This program simulates (n) hands of blackjack for each possible")
    print("starting card and displays the probability of the dealer busting")
    print("for a particular draw.")
    print("Enter the number of iterations you would like the simulation to")
    print("perform. Note: the higher the number, the more precise the results.")
    print("Enter a number greater than 100.")
def simNHands(n, startCard):
    print(startCard)
    busts = 0
    for i in range(n):
        if not simOneHand(startCard):
            busts = busts + 1
    return busts

def simOneHand(startCard):
    x = startCard
    if x == 11 or x == 12 or x == 13:
        x = 10
    y = simOneCard()
    hand = x + y

    while hand < 17:
        if hasAce(x) is False and hasAce(y) is False:
            z = simOneCard()
            if hasAce(z) is False:
                hand = hand + z
            else:
                if 10 >= hand >= 6:
                    hand = hand + 11
                else:
                    hand = hand + 1
        elif hasAce(x) is True and hasAce(y) is True:
            z = simOneCard()
            if hasAce(z) is False:
                hand = hand + z
                if 10 >= hand >= 6:
                    hand = hand + 11
                else:
                    hand = hand + 1
            else:
                if 10 >= hand >= 6:
                    hand = hand + 11
                else:
                    hand = hand + 1

        else:
            if 10 >= hand >= 6:
                hand = hand + 11
            else:
                if hand < 15:
                    z = simOneCard()
                    hand = hand + 1 + z
                else:
                    break
    if hand > 21:
        #bust
        return False
    else:
        return True

def simOneCard():
    x = randrange(1, 13)
    if x == 11 or x == 12 or x == 13:
        x = 10
        return x
    else:
        return x

def hasAce(x):
    if x == 1:
        return True
    else:
        return False

def printSummary(busts, n, i):
    cards = ['1','Ace', '2', '3', '4','5','6','7','8','9','10','Jack','Queen','King']
    print()
    print("{0}: {1:0.1%} ".format(cards[i],busts/n))

if __name__ == '__main__': main()
