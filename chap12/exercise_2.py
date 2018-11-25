#objrball   -- Simulation of Tennis Matches
#           Illustrates design with objects.

from random import random
from consolereader import ConsoleReader

class Player:
    #A Player keeps track of service probability and score

    def __init__(self, prob):
        #Create a player with this probability
        self.prob = prob
        self.score = 0
        self.game = 0
        self.set = 0
        self.match = 0

    def winsServe(self):
        #Returns a Boolean that is true with probability self.prob
        return random() <= self.prob

    def getProb(self):
        return self.prob

    def incScore(self):
        #Add a point to this player's score
        self.score = self.score + 1
    
    def incGames(self):
        self.game = self.game + 1
    
    def incSets(self):
        self.set = self.set + 1
    
    def incMatches(self):
        self.match = self.match + 1

    def getScore(self):
        #Returns this player's current game score
        return self.score

    def getGame(self):
        return self.game
    
    def getSet(self):
        return self.set
    
    def getMatch(self):
        return self.match



class TennisMatch:
    #A TennisMatch represents a match in progress. A match has two players
    #and keeps track of which one is currently serving

    def __init__(self,  probA, probB):
        #Create a new game having players with the given probs.
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA #Player A always serves first
    
    def playGame(self):
        #Play the game to completion
        y = self.playerA.getProb()
        while not self.isOverGame():
            x = random()
            if x < y:
                self.playerA.incScore()
            else:
                self.playerB.incScore()
        
    def isOverGame(self):
        #Returns game is finished (i.e. one of the players has won).
        a, b = self.getScores()
        if (a >= 4) or (b >= 4):
            if abs(a-b) >=2:
                if a > b:
                    self.playerA.incGames()
                else:
                    self.playerB.incGames()
                return True
            else:
                return False
        else:
            return False    
    
    def playSet(self):
        self.playGame()
        a, b = self.getGames()
        while not self.isOverSet():
            if a > b:
                self.playerA.incSets()
            else:
                self.playerB.incSets()

    def isOverSet(self):
        a, b = self.getSets()
        if a == 7 or b == 7:
            return True
        elif a >= 6 or b >= 6:
            if abs(a-b) >=2:
                return True
            else:
                return False
        else:
            return False

    def playMatch(self):
        self.playSet() 
        a, b = self.getSets()
        while not self.isOverMatch():
            if a > b:
                self.playerA.incMatches()
            else:
                self.playerB.incMatches()

    def isOverMatch(self):
        a, b = self.getMatches()
        if a > 3 or b > 3:
            return True
        else:
            return False

    def changeServer(self):
        #Switch which player is serving
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA
    
    def getScores(self):
        #Returns the current game scores of player A and player B
        return self.playerA.getScore(), self.playerB.getScore()
    
    def getGames(self):
        #Returns the current games won by player A and player B
        return self.playerA.getGame(), self.playerB.getGame()

    def getSets(self):
        #Returns the current sets won by player A and player B
        return self.playerA.getSet(), self.playerB.getSet()

    def getMatches(self):
        #Returns the current matches won by player A and player B
        return self.playerA.getMatch(), self.playerB.getMatch()

class SimStats:
    #SimStats handles accumulation of statistics across multiple
    #   (completed) matches. This version tracks the wins for 
    #   each player.
    def __init__(self):
        #Create a new accumulator for a series of matches
        self.winsA = 0 
        self.winsB = 0

    def update(self, aMatch):
        #Determine the outcome of aMatch and update statistics
        a, b = aMatch.getMatches()
        if a > b:
            self.winsA = self.winsA + 1
        else:
            self.winsB = self.winsB + 1
    
    def printReport(self):
        #Print a nicely formatted report
        n = self.winsA + self.winsB
        print("Summary of", n, "matches:\n")
        print("         wins (% total)")
        print("---------------------------")
        self.printLine("A", self.winsA, n)
        self.printLine("B", self.winsB, n)

    def printLine(self, label, wins, n):
        template = "Player {0}:{1:5}    ({2:5.1%})"
        print(template.format(label, wins, float(wins)/n))

def printIntro():
    print("This program simulates matches of tennis between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point on the serve.")

def getInputs():
    #Returns the three simulation parameters
    a = None
    b = None
    n = None
    while (a == None) or (b == None) or (n == None):
        a = ConsoleReader.read_float("What is the prob. player A? ")
        b = ConsoleReader.read_float("What is the prob. player B? ")
        n = ConsoleReader.read_int("How many matches? ")
    # a = eval(input("What is the prob. player A wins a serve? "))
    # b = eval(input("What is the prob. player B wins a serve? "))
    # n = eval(input("How many matches to simulate? "))
    return a, b, n

def main():
    printIntro()
    probA, probB, n = getInputs()
    #Play the matches
    stats = SimStats()
    for i in range(n):
        theGame = TennisMatch(probA, probB) #create a new game
        theGame.playMatch()                    #Play it
        stats.update(theGame)             #Extract info

    #Print the results
    stats.printReport()

main()
input("\nPress <Enter> to quit")