from graphics import *
import math as m

def main():
    #Create a square window and set coordinates -10,-10 to 10,10
    win = GraphWin("Intersection of a line through a Circle", 500,500)
    win.setCoords(-10, -10, 10, 10)

    #Input: Radius of the circle and the y-intercept of the line
    r = eval(input("What is the radius of the circle? "))
    y = eval(input("Where does the line cross the y axis? "))

    #Draw a circle centered at 0,0
    c = Circle(Point(0,0), r)
    c.draw(win)

    #Draw a horizontal line across the window with teh given y-intercept
    line = Line(Point(-10, y), Point(10, y))
    line.draw(win)

    if r < y:
        print("The line does not intersect.")
    else:
        #Compute x
        x = m.sqrt(r**2 - y**2)

        #Print the two x values of intersection textually
        print(-x, x)

        #Print the two x values graphically
        x1 = Text(Point(-x, y + 2),-x)
        x2 = Text(Point(x, y + 2), x)
        x1.draw(win)
        x2.draw(win)

main()
