from graphics import *

def main():
    win = GraphWin("Welcome Home", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    #2 clicks for the frame of the house
    message = Text(Point(0, 8), "Click on 2 diagonal points to create the rectangular frame of your house.")
    message.draw(win)
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    y1 = point1.getY()
    x2 = point2.getX()
    y2 = point2.getY()
    r = Rectangle(point1, point2)
    r.draw(win)
    message.undraw()

#The third click will show the center of the top of the door
    message = Text(Point(0, y1-1), "Excellent! Click the top of the door frame.")
    message.draw(win)
    point3 = win.getMouse()
    x3 = point3.getX()
    y3 = point3.getY()

    #door width is 1/5 house width
    r_width = x2 - x1
    door = Rectangle(Point(x3-(1/10 * r_width), y1), Point(x3+(1/10 * r_width), y3))
    door.draw(win)
    message.setText("Now click to place a window.")

#Click four will print a square window
    point4 = win.getMouse()
    x4 = point4.getX()
    y4 = point4.getY()
    #window is 1/2 width door (z is variable for distance off center)
    z = 1/20 * r_width
    window = Rectangle(Point((x4-z), (y4-z)), Point((x4+z), (y4+z)))
    window.draw(win)
    message.setText("Finally, click the crown of the roof!")

#Click five will indicate peak of roof
    point5 = win.getMouse()
    line1 = Line(point2, point5)
    line1.draw(win)
    line2 = Line(point5, Point(x1, y2))
    line2.draw(win)
    message.setText("Welcome, to your new home.")

    win.getMouse()
    win.close()

main()
