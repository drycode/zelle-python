import math as m
from graphics import *

def main():
    win = GraphWin("Line Drawing Tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)
#Prompt the User for 2 mouse clicks
    message = Text(Point(-5, 8), "Click on 2 points to create a line")
    message.draw(win)
#Store coordinates in variables x1, x2 etc
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

#Create a Line w/ midpoint "cyan"
    line = Line(point1, point2)
    line.draw(win)
    mx, my = (x1+x2)/2, (y1+y2)/2
    win.plot(mx, my, "cyan")

#Calculate the length and slope of the Line
    length = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if (x2 - x1) == 0:
        message3 = Text(Point(-5,6), ("The slope of the line is vertical."))
    else:
        slope = (y2-y1)/(x2 -x1)
        message3 = Text(Point(-5, 6), ("The slope of the line is: ", round(slope, 2)))
#Print length and slope of line
    message2 = Text(Point(-5, 7), ("The length of the line is: ", round(length, 2)))
    message2.draw(win)
    message3.draw(win)

main()
