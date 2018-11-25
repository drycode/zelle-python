#Skunk Game
from random import randrange

class Dice:
    def __init__(self):
        self.dice = [0] * 2
        self.rollDice()

    def rollDice(self):
        for i in range(len(self.dice)):
            self.dice[i] = randrange(1,7)
        
    def values(self):
        return self.dice[:]

class SkunkApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface
        self.players = []
        self.makeplayers()
    
    def run(self):
        while not self.gameOver():
            self.interface.newRound()
            self.refreshPlayers()
            print("Round: {}".format(self.interface.getRound() + 1))
            print("\n")
            self.playRound()
        self.interface.gameSummary(self.players)

    def playRound(self):
        books = self.interface.getRound()
        while not self.roundOver():
            for player in self.players:
                if player.active():
                    values = self.doRoll(player)
                    if values != [0, 0]:
                        x, y = values[0], values[1]
                        if x == 1 and y == 1:
                            player.resetRoundScores(books)
                        elif x ==1 or y == 1:
                            player.reset_rScore()
                        else:
                            player.inc_Score(x + y, books)
                        self.interface.currentscores(values, self.players)       
        for player in self.players:
            player.tallyRound(books)
        
    def refreshPlayers(self):
        for player in self.players:
            player.reactivate()
            player.rScoreOnly()

    def doRoll(self, player):
        if self.interface.rollAgain(player.getName()):
            self.dice.rollDice()
            values = self.dice.values()
            return values
        else:
            player.deactivate()
            return [0, 0]
    
    def makeplayers(self):
        for name in self.interface.getPlayerNames():
            x = Player(name)
            self.players.append(x)

    def roundOver(self):
        over = True
        for player in self.players:
            if player.active():
                over = False
        return over        

    def gameOver(self):
        if self.interface.getRound() >= 4:
            return True

class Player:
    def __init__(self, name):
        self.name = name
        self.rScore = 0
        self.totScore = 0
        self.roundScores = [0] * 5
        self.play = True

    def getName(self):
        return self.name

    def tallyRound(self, book):
        self.roundScores[book] = self.get_rScore()
    
    def resetRoundScores(self, books):
        prevRoundScores = 0
        for num in self.roundScores:
            prevRoundScores += num
        self.totScore -= prevRoundScores
        for i in range(books):
            self.roundScores[i] = 0
        self.play = False

    def inc_Score(self, score, books):
        self.totScore = self.totScore + score
        prevRoundScores = 0
        for num in self.roundScores[0:books]:
            prevRoundScores += num
        self.rScore = self.totScore - prevRoundScores


    def reset_rScore(self):
        self.totScore -= self.rScore
        self.rScore = 0
        self.play = False

    def get_rScore(self):
        return self.rScore
    
    def get_roundScores(self):
        return self.roundScores
    
    def get_totScore(self):
        return self.totScore
        
    def active(self):
        return self.play
    
    def reactivate(self):
        self.play = True

    def deactivate(self):
        self.play = False
    
    def rScoreOnly(self):
        self.rScore = 0

class TextInterface:
    def __init__(self):
        self.round = -1
    
    def getRound(self):
        return self.round

    def newRound(self):
        self.round = self.round + 1
        return self.round
        print()
        print("Entering Round {}".format(self.__whichRound()))
    
    def setDice(self, values):
        print("You rolled {}.".format(values))
        print("\n")
    
    def __whichRound(self):
        letter = ["S", "K", "U", "N", "K"]
        return letter[self.round]
    
    def gameOver(self, name):
        print("The Game is Over. {} wins!".format(name))
    
    def currentscores(self, values, players):
        for player in players:
            name = player.getName()
            rScore = player.get_rScore()
            totscore = player.get_totScore()
            print("Player: {0}    Score: {1}     Total: {2}".format(name, rScore, totscore))
        self.setDice(values)
    
    def finalScores(self, players):
        print("Name: {0:>10}{1:>10}{2:>10}{3:>10}{4:>10}{5:>10}".format("S", "K", "U", "N", "K", "Total"))
        print("-------------------------------------------------------------------")
        for player in players:
            scores = player.get_roundScores()
            name = player.getName()
            totscore = player.get_totScore()
            print("{0:5}:{1:>10}{2:>10}{3:>10}{4:>10}{5:>10}{6:>10}".format(name, scores[0], scores[1], scores[2], scores[3], scores[4], totscore))

    def rollAgain(self, name):
        ans = None
        while ans == None:
            ans = input("Do you wish to roll again {}? >> ".format(name))
            if ans[0] in "yY":
                return True
            elif ans[0] in "nN":
                return False
            else:
                ans = None
                print("Sorry, I don't understand.")            
    
    def getPlayerNames(self):
        totplayers = []
        x = 0
        while x != '':
            x = input("Enter a players name (<Enter> to Continue) >> ")
            totplayers.append(x)
        totplayers.remove('')
        return totplayers

    def gameSummary(self, players):
        print("The game is over.")
        self.finalScores(players)

def main():
    inter = TextInterface()
    app = SkunkApp(inter)
    app.run()

main()
    