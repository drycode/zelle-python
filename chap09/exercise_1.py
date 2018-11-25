from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    matchA, matchB = simNMatches(n, probA, probB)
    printSummary(matchA, matchB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("reflects the likelihood of a player winning the serve.")
    print("Player A has the first serve.")

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
    for i in range(n):
        winsA, winsB = simOneMatch(probA, probB)

        if winsA > winsB:
            matchA = matchA + 1
        else:
            matchB = matchB + 1
    return matchA, matchB

def simOneMatch(probA, probB):
    winsA = winsB = 0
    #accumulate number of games
    x = 1
    while winsA !=2 and winsB !=2:
        scoreA, scoreB = simOneGame(probA, probB, x)
        if scoreA > scoreB:
            winsA = winsA + 1
            x = x+1
        else:
            winsB = winsB + 1
            x = x+1
    return winsA, winsB

def simOneGame(probA, probB, x):
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
    return scoreA, scoreB

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

def printSummary(matchA, matchB):
    # Prints a summary of wins for each players
    n = matchA + matchB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(matchA, matchA/n))
    print("Wins for B: {0} ({1:0.1%})".format(matchB, matchB/n))

if __name__ == '__main__': main()
