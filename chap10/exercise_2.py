#graphical program to trace random walk in 2 dimensions

import math as m
from random import random
from graphics import *
from button import Button

def main():
    n = 100
    win = GraphWin("Random Walk", 1200, 1200)
    win.setCoords(-100, -100, 100, 100)

    newWalk = Button(win, Point(-80, -80), 30, 20, "Random Walk")
    quitButton = Button(win, Point(80, -80), 30, 20, "Quit")
    newWalk.activate()
    pt = win.getMouse()
    point = Point(0, 0)

    while not quitButton.clicked(pt):
        newWalk.deactivate()
        randWalk(n, win, point)
        newWalk.activate()
        quitButton.activate()
        pt = win.getMouse()
        while not (newWalk.clicked(pt) or quitButton.clicked(pt)):
            pt = win.getMouse()
        point = Point((2 * random() - 1) * 80, (2 * random() - 1) * 80)
    win.close()




def randWalk(n, win, point):
    point2 = point
    for i in range (n):
        x = point2.getX()
        y = point2.getY()

        point1 = simOneStep(x, y)
        point1.draw(win)
        line = Line(point2, point1)
        line.draw(win)
        point2 = point1

def simOneStep(x, y):
    angle = random() * 2 * m.pi
    x = x + m.cos(angle)
    y = y + m.sin(angle)
    point = Point(x, y)
    return point

if __name__ == '__main__': main()
