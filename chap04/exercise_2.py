from graphics import *

def main():
    win = GraphWin()
    win.setCoords(0, 0, 10, 10)
    c = Circle(Point(5,5), 5)
    c.setOutline("green4")
    c.setFill("white")
    c.setWidth(5)
    c.draw(win)

    c2 = Circle(Point(5,5), 4)
    c2.setOutline("green4")
    c2.setFill("red")
    c2.setWidth(5)
    c2.draw(win)

    c3 = Circle(Point(5,5), 3)
    c3.setOutline("green4")
    c3.setFill("blue")
    c3.setWidth(5)
    c3.draw(win)

    c4 = Circle(Point(5,5), 2)
    c4.setOutline("green4")
    c4.setFill("black")
    c4.setWidth(5)
    c4.draw(win)

    c5 = Circle(Point(5,5), 1)
    c5.setOutline("green4")
    c5.setFill("white")
    c5.setWidth(5)
    c5.draw(win)
main()
