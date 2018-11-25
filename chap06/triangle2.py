import math
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
            + square(p2.getY() - p1.getY()))
    return dist
import math as m
def triArea(a, b, c):
    s = (a + b + c) / 2
    A = m.sqrt(s * (s-a) * (s-b) * (s-c))
    return A

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    #Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    #Calculate the perimeter of the Triangle
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText("The perimeter is: {0:0.2f}".format(perim))

    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)

    A = triArea(a, b, c)
    message2 = Text(Point(5, 1.5), "The area is {0:0.2f}".format(A))
    message2.draw(win)

    #Wait for another click to exit
    win.getMouse()
    win.close

main()
