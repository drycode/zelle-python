from graphics import *

def main():
    win = GraphWin()
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    square = Rectangle(Point(4,4), Point(6,6))
    square.setOutline("red")
    square.setFill("red")
    square.draw(win)
    for i in range(10): 
        p = win.getMouse()
        c = square.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        s2 = square.clone()
        s2.draw(win)
        s2.move(dx, dy)
        square = s2
    message = Text(Point(5,9),"Click anywhere to close")
    message.draw(win)
    win.getMouse()
    win.close()
main()
