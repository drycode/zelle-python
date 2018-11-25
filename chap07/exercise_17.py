from graphics import *
from time import sleep
import math as m

def main():
    win = GraphWin("Bouncing Ball", 500, 500)
    win.setCoords(-100, -100, 100, 100)

    shape = Circle(Point(0,-80),20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    dx = 1
    dy = 1

    for i in range(10000):
        c = shape.getCenter()
        
        if c.getX() > 80:
            dx = -1
        elif c.getX() < -80:
            dx = 1
        elif c.getY() > 80:
            dy = -1
        elif c.getY() < -80:
            dy = 1
           
        sleep(0.005)
        shape.move(dx,dy)
main()
