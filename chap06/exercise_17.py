from graphics import *

def moveTo(shape, newCenter, win):
    dx = oldCenter.getX() - newCenter.getX()
    dy = oldCenter.getY() - newCenter.getY()

    shape.move(dx, dy)
    #shape.draw(win)

def main():
    win = GraphWin("Move Shape", 400, 400)
    win.setCoords(0, 0, 100, 100)

    oldCenter = win.getMouse()
    shape = Circle(oldCenter, 3)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        newCenter = win.getMouse()
        moveTo(shape, newCenter, win)
    win.close()
main()
