#This program with graphically plot a regression line

from graphics import *
import math as m

def graphWin(Title):
#Create a graphics window with <done> button in bottom left corner
    win = GraphWin(Title, 400, 400)
    win.setCoords(-10, -10, 10, 10)
    #Tell user to select multiple locations on the screen to designate points
    message = Text(Point(-5, 8), "Click to delineate points on the graph.")
    message.draw(win)

    axisX = Line(Point(-10,0), Point(10,0))
    axisX.draw(win)

    axisY = Line(Point(0,10), Point(0,-10))
    axisY.draw(win)

    r = Rectangle(Point(-9, -9), Point(-7,-8))
    r.draw(win)
    rCenter = r.getCenter()
    stopMouse = Text(rCenter, "Done")
    stopMouse.draw(win)

    #Accept input from user until <done> button is pressed
    click = Point(0,0)
    allPoints = []
    while True:
        click = win.getMouse()
        if ((-9 <= click.getX() <= -7) and (-9 <= click.getY() <= -8)):
            break
        else:
            #Store user points in an appended list
            allPoints.append(click)
            click.draw(win)
    return allPoints, win

def average(allPoints):
    #https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/regression-analysis/find-a-linear-regression-equation/
    sumX = 0
    sumY = 0
    count = 0
    sumXiYi = 0
    sumSqXi = 0
    sumSqYi = 0
    for i in allPoints:
        x = i.getX()
        y = i.getY()
        sumX = sumX + x
        sumY = sumY + y
        count = count + 1
        xy = x * y
        sumXiYi = sumXiYi + xy
        SqX = x * x
        sumSqXi = sumSqXi + SqX
        SqY = y * y
        sumSqYi = sumSqYi + SqY

    a = ((sumY * sumSqXi) - (sumX * sumXiYi)) / (count * (sumSqXi) - sumX ** 2)
    b = ((count * sumXiYi) - (sumX * sumY)) / (count * (sumSqXi) - sumX ** 2)

    return a, b

def main():
    allPoints, win = graphWin("Regression Line")
    a, b = average(allPoints)
    x1 = -10
    x2 = 10
    regressLine = Line(Point(x1, (a + b * x1)), Point(x2, (a + b * x2)))
    regressLine.draw(win)
    win.getMouse()
main()
