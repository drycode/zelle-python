from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, n)

def printIntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B". The abilities of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("reflects the likelihood of a team winning the serve.")
    print("Starting serve alternates each game. Players win the serve with")
    print("a winning volley, and can score on either teams serve per Rally rules.")

def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    #Simulates a single game of volleyball between players whose
    #   abilities are represented by the probability of winning a serve.
    #Returns final scores for A and B
    #starting serve alternates each game
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, n)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB, n):
    #Simulates a single game of volleyball between players whose
    #   abilities are represented by the probability of winning a serve.
    #Returns final scores for A and B
    #starting serve alternates each game
    serving = findService(n)
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
                scoreB = scoreB + 1
        elif serving == "B":
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
                scoreA = scoreA + 1
    return scoreA, scoreB

def findService(n):
    if n % 2 == 0:
        return "A"
    else:
        return "B"

def gameOver(a, b):
    #a and b represent scores for a racquetball game
    #Returns True if the game is over, False otherwise
    if a > 25 or b > 25:
        if abs(a-b) >= 2:
            return True
        else:
            return False
    else:
        return False

def printSummary(winsA, winsB, n):
    # Prints a summary of wins for each players
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
