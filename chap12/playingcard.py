#playingcard.py
from graphics import *
import Playing_Card_Images

class PlayingCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        if 10 <= self.rank <= 13:
            self.rank = 10
        else:
            self.rank = self.rank
        return self.rank

    def __str__(self):
        n = self.rank
        if self.suit == 'D':
            s = "Diamonds"
        elif self.suit == 'S':
            s = "Spades"
        elif self.suit == 'H':
            s = "Hearts"
        else:
            s = "Clubs"

        rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        self.cardname = "{0} of {1}".format(rank[n - 1], s)
        return self.cardname

    def draw(self, win, center):
        filename = "./Playing_Card_Images/{0}{1}.png".format(self.rank, self.suit.upper())
        card = Image(center, filename)
        card.draw(win)
    
class Deck:
    def __init__(self):
        rank = ['C','D','H','S']
        cardSpecs = []
        for i in range(52):
            x = i % 13 + 1
            y = rank[i % 4]
            cardSpecs.append((x,y))
        self.cards = []
        for (x, y) in cardSpecs:
            self.cards.append(PlayingCard(x, y))
    
    def __shuffle(self):
        newList = []
        for i in range (len(self.cards)):
            x = int(random() * len(self.cards)) - 1
            newList.append(self.cards[x])
            self.cards.remove(self.cards[x])
        return newList

    def shuffle(self):
        self.cards = self.__shuffle()
    
    def dealCard(self):
        return self.cards.pop(0)

    def cardsLeft(self):
        return len(self.cards)