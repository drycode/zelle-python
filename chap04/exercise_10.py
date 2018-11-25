from graphics import *
import math as m

def main():
    win = GraphWin("Line Drawing Tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)
#Prompt the User for 3 mouse clicks
    message = Text(Point(-5, 8), "Click on 3 points to create a Triangle")
    message.draw(win)

#Store coordinates in variables x1, x2 etc
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    x3 = point3.getX()
    y3 = point3.getY()
#Calculate Perimeter
    a = m.sqrt((x2-x1)**2 + (y2-y1)**2)
    b = m.sqrt((x3-x1)**2 + (y3-y1)**2)
    c = m.sqrt((x3-x2)**2 + (y3-y2)**2)
    perimeter = a + b + c
#Calculate Area
    s = perimeter/2
    area = m.sqrt(s*(s-a)*(s-b)*(s-c))

#Draw Rectangle
    line1 = Line(point1, point2)
    line1.draw(win)
    line2 = Line(point2, point3)
    line2.draw(win)
    line3 = Line(point3, point1)
    line3.draw(win)
#Print the Perimeter and area of the rectangle
    message2 = Text(Point(-5, 7), ("The area of the triangle is", round(area, 2)))
    message2.draw(win)
    message3 = Text(Point(-5, 6), ("The perimeter of the triangle is", round(perimeter, 2)))
    message3.draw(win)

main()
