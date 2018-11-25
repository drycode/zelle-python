from textpoker import TextInterface
from pokerapp import PokerApp
from dieview import DieView
from graphics import *
from button import Button

class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        
        #Splash screen with introduction, let's play and exit buttons
        self.splashScreen()

        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        #Add help button that initialized new window Help
        b = Button(self.win, Point(570, 25), 40, 30, "Help")
        self.buttons.append(b)
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)
        
    
    def splashScreen(self):
        play = Button(self.win, Point(300, 230), 400, 40, "Let's Play")
        _exit = Button(self.win, Point(570, 375), 40, 30, "Exit")
        intro = Text(Point(300, 380), "Welcome to the Game. Would you like to Play?")
        
        intro.setSize(18)
        for i in [play, _exit]:
            i.activate()
        click = Point(0,0)
        while not play.clicked(click): 
            click = self.win.getMouse()
            if _exit.clicked(click):
                self.win.close()
            elif play.clicked(click):
                play.undraw()
                _exit.undraw()
                intro.undraw()\
                

    def createDice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)
    
    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1, 6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)
            
    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score) 
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)
    
    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])
    
    def choose(self, choices):
        buttons = self.buttons

        #activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        
        #get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() #function exit here
    
    def wantToPlay(self):
        ans = ""
        while ans != "Quit":
            ans = self.choose(["Roll Dice", "Quit", "Help"])
            self.msg.setText("")
            if ans == "Help":
                self.getHelp()
            else:
                return ans == "Roll Dice"

    def chooseDice(self):
        #choices is a list of the indexes of the selected dice
        choices = []            #no dice chosen yet
        while True:
            #wiat for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5", "Roll Dice", "Score"])

            if b[0] == "D":         #User clicked a die Button
                i = eval(b[4]) - 1  #Translate label to die index
                if i in choices:    #Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:                   #User clicked Roll or Score
                for d in self.dice: #Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":    #Score clicked, ignore choices
                    return []
                elif choices != []: #Don't accept Roll unless some
                    return choices  #   dice are actually selected

    def getHelp(self):
        win2 = GraphWin("Help Window", 600, 400)
        win2.setBackground("green3")
        help = 'This game of dice poker allows the user to roll for hands "(5-3)-of-a-kind",\
        \n"Full House", "Straight", etc. Each round consists of up to three rolls. the user\n \
        will select the appropriate dice to re-roll. If no dice are chosen, the user will be scored\
        \n based on the initial roll.\n'
        payouts = "{0:<100}{1:>0}\n-------------------------------\
        --------------------------------\n".format("Hands", "Pay")
        hand_specs = [("Two Pairs", 5), ("Three of a Kind", 8), ("Full House", 12), ("Four of a Kind", 15), ("Straight (1-5 or 2-6)", 20), ("Five of a Kind", 30)]
        for (hand, pay) in hand_specs:
            payouts = payouts + '{0:<100} ${1:>0.2f}\n'.format(hand, pay)
        msg = Text(Point(300, 100), help)
        msg.setSize(14)
        msg2 = Text(Point(300, 300), payouts)
        msg.draw(win2)
        msg2.draw(win2) 
        win2.getMouse()
        win2.close()       

    def close(self):
        self.win.close()

def main():
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()
    #Expand by printig high score data to JSON File

main()