from playingcard import PlayingCard
from graphics import *
from random import random

def main():
    win = GraphWin("Playing Card", 700, 1100)
    win.setCoords(-10, -10, 10, 10)

    n = 5
    for i in range (n):
        x = int(random() * 13) + 1
        y = int(random() * 4)
        suit = ['d', 's', 'h', 'c']
        card = PlayingCard(x, suit[y])
        card.draw(win, Point(0,0))
        win.getMouse()
        
main()

