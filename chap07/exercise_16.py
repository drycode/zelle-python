from graphics import *
import math as m

def main():
    win = GraphWin()
    win.setCoords(-5, -5, 5, 5)
    c = Circle(Point(0,0), 5)
    c.setOutline("green4")
    c.setFill("white")
    c.setWidth(1)
    c.draw(win)

    c2 = Circle(Point(0,0), 4)
    c2.setOutline("green4")
    c2.setFill("red")
    c2.setWidth(1)
    c2.draw(win)

    c3 = Circle(Point(0,0), 3)
    c3.setOutline("green4")
    c3.setFill("blue")
    c3.setWidth(1)
    c3.draw(win)

    c4 = Circle(Point(0,0), 2)
    c4.setOutline("green4")
    c4.setFill("black")
    c4.setWidth(1)
    c4.draw(win)

    c5 = Circle(Point(0,0), 1)
    c5.setOutline("green4")
    c5.setFill("white")
    c5.setWidth(1)
    c5.draw(win)

    sum = 0
    for x in range (5):
        arrow = win.getMouse()
        x = arrow.getX()
        y = arrow.getY()
        z = m.sqrt(x ** 2 + y ** 2)
        
        if 5 >= z > 4:
            y = 1
            sum = y + sum
        elif 4 >= z > 3:
            y = 3
            sum = y + sum
        elif 3 >= z > 2:
            y = 5
            sum = y + sum
        elif 2 >= z > 1:
            y = 7
            sum = y + sum
        elif 1 > z:
            y = 9
            sum = y + sum
        else:
            y = 0
            print("You missed!")
        print("Point: {0}    Total: {1}".format(y, sum))

main()
