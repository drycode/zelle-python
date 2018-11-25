from playingcard import PlayingCard
from random import random
from graphics import GraphWin, Point

def main():
    win = GraphWin("Playing Card", 700, 1100)
    win.setCoords(-10, -10, 10, 10)
    
    #create 52 card (13 per suit) parameters    
    rank = ['C','D','H','S']
    cardSpecs = []
    for i in range(52):
        x = i % 13 + 1
        y = rank[i % 4]
        cardSpecs.append((x,y))
    cards = []
    for (x, y) in cardSpecs:
        cards.append(PlayingCard(x, y))
   
    cards.sort(key=PlayingCard.getRank)
    cards.sort(key=PlayingCard.getSuit)
    for card in cards:   
        card.draw(win, Point(0,0))
main()
