from zelle_modules.regression import Regression
from graphics import *

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
    return win


def main():
    win = graphWin("Regression Line")
    allPoints = []
    bestfit = Regression(win, allPoints, -10, 10)
    click = win.getMouse()
    click.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    bestfit.addPoint(p1)
    bestfit.addPoint(click)
    bestfit.drawRegressionLine(win)

    while True:
        click = win.getMouse()
        if ((-9 <= click.getX() <= -7) and (-9 <= click.getY() <= -8)):
            break
        else:
            #Store user points in an appended list
            bestfit.addPoint(click)
            click.draw(win)
            bestfit.unDraw()
            bestfit.drawRegressionLine(win)
if __name__ == '__main__': main()