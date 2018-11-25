#playingcard.py
from graphics import *
import sys
import os

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
        if self.suit == 'd':
            s = "Diamonds"
        elif self.suit == 's':
            s = "Spades"
        elif self.suit == 'h':
            s = "Hearts"
        else:
            s = "Clubs"

        rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        self.cardname = "{0} of {1}".format(rank[n - 1], s)
        return self.cardname

    def draw(self, win, center):
        filename = "{0}{1}".format(self.rank, self.suit.upper())
        card = Image(center, filename)
        card.draw(win)
