from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    matchA, matchB, shutA, shutB = simNMatches(n, probA, probB)
    printSummary(matchA, matchB, shutA, shutB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("reflects the likelihood of a player winning the serve.")
    print("Starting serve alternates each game, but Player A starts each match.")
    print()

def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNMatches(n, probA, probB):
    #Simulates n Matches of racquetball between players whos
    #   abilities are represented by the probability of winning a serve.
    #Returns number of match wins for A and B. Matches are determined
    #by best of 3 games. Service alternates per game
    matchA = matchB = 0
    shutA = shutB = 0

    for i in range(n):
        winsA, winsB, shutA, shutB = simOneMatch(probA, probB, shutA, shutB)

        if winsA > winsB:
            matchA = matchA + 1
        else:
            matchB = matchB + 1
    return matchA, matchB, shutA, shutB

def simOneMatch(probA, probB, shutA, shutB):
    winsA = winsB = 0
    #accumulate number of games
    x = 1
    while winsA !=2 and winsB !=2:
        scoreA, scoreB, shutA, shutB = simOneGame(probA, probB, x, shutA, shutB)
        if scoreA > scoreB:
            winsA = winsA + 1
            x = x+1
        else:
            winsB = winsB + 1
            x = x+1
    return winsA, winsB, shutA, shutB

def simOneGame(probA, probB, x, shutA, shutB):
    #Simulates a single game of racquetball between players whoe
    #   abilities are represented by the probability of winning a serve.
    #Returns final scores for A and B
    serving = findService(x)
    scoreA = 0
    scoreB = 0


    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        elif serving == "B":
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    if scoreA == 7:
        shutA = shutA + 1
    if scoreB == 7:
        shutB = shutB + 1
    return scoreA, scoreB, shutA, shutB

def findService(x):
    if x % 2 == 0:
        return "A"
    else:
        return "B"

def gameOver(a, b):
    #a and b represent scores for a racquetball game
    #Returns True if the game is over, False otherwise
    #Must win by 2
    #7-0 is a shutout

    if a == 0 and b == 7:
        return b == 7
    elif b == 0 and a == 7:
        return a == 7
    elif abs(a-b) >= 2:
        return True
    else:
        return False

def printSummary(matchA, matchB, shutA, shutB):
    # Prints a summary of wins for each players
    n = matchA + matchB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(matchA, matchA/n))
    print("Wins for B: {0} ({1:0.1%})".format(matchB, matchB/n))
    print()
    print("Shutouts for A: {0} ({1:0.1%})".format(shutA, shutA/matchA))
    print("Shutouts for B: {0} ({1:0.1%})".format(shutB, shutB/matchB))

if __name__ == '__main__': main()
