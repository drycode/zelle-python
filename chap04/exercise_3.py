from graphics import *

def main():
    win = GraphWin("Face", 900, 900)
    win.setCoords(0,0,10,10)
    head = Oval(Point(1.5,0.75), Point(8.5,9.25))
    head.draw(win)

    c = Circle(Point(4.1, 6.75), .75)
    c.draw(win)

    c2 = c.clone()
    c2.move(2, 0)
    c2.draw(win)

    mouth = Rectangle(Point(3,3),Point(7,4))
    mouth.draw(win)

    teeth = Rectangle(Point(3,3), Point(3.5, 4))
    teeth.draw(win)

    for i in range (7):
        t2 = teeth.clone()
        t2.move(.5, 0)
        t2.draw(win)
        teeth = t2

    lip = Line(Point(3,3.5), Point(7,3.5))
    lip.draw(win)
main()
