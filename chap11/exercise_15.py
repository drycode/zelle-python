from playingcard import PlayingCard
from random import random

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

def main():
    deck = Deck()
    deck.shuffle()
    for i in range(52):
        print(deck.dealCard())
main()


