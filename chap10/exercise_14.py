from face import Face
from graphics import *
from time import sleep
import math as m

#Modify the face class from the previous problem to include a move
#method similar to other grahpics objects. Using the move method, create a
#program that makes a face bounce around in a window (see Programming Ex17
#Chap7). Bonus: have the face change expression each time it "hits" the edge
#of the window.

#Bonus incomplete

def main():
    win = GraphWin("Bouncing Face", 500, 500)
    win.setCoords(100, 100, -100, -100)

    face = Face(win, Point(0,0), 15)

    dx = 5
    dy = 5

    for i in range(10000):
        c = face.getCenter()
        
        if c.getX() > 80:
            dx = -5
        elif c.getX() < -80:
            dx = 5
        elif c.getY() > 80:
            dy = -5
        elif c.getY() < -80:
            dy = 5
        sleep(0.005)
        face.move(dx,dy)
main()
