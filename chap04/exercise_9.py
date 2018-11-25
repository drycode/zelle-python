from graphics import *

def main():
    win = GraphWin("Line Drawing Tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)
#Prompt the User for 2 mouse clicks
    message = Text(Point(-5, 8), "Click on 2 points to create a Rectangle")
    message.draw(win)

#Store coordinates in variables x1, x2 etc
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
#Calculate Perimeter and Area
    area = (x2 - x1)*(y2 - y1)
    perimeter = 2 * ((x2-x1)+(y2-y1))
#Draw Rectangle
    r = Rectangle(point1, point2)
    r.draw(win)
#Print the Perimeter and area of the rectangle
    message2 = Text(Point(-5, 7), ("The area of the rectangle is", round(area, 2)))
    message2.draw(win)
    message3 = Text(Point(-5, 6), ("The perimeter of the rectangle is", round(perimeter, 2)))
    message3.draw(win)

main()
