from graphics import *

class Regression: 
    def __init__(self, window, allPoints, max_x_win, min_x_win):
        self.window = window
        self.allPoints = allPoints
        self.max_x_win = max_x_win
        self.min_x_win = min_x_win

    def addPoint(self, click):
        self.allPoints.append(click)

    def __computeSlope(self):
        sumX = 0
        sumY = 0
        count = 0
        sumXiYi = 0
        sumSqXi = 0
        sumSqYi = 0
        for i in self.allPoints:
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

    def predict(self, x_value):
        a, b = self.__computeSlope()
        x = x_value
        y = b * x + a

        return y

    def unDraw(self):
        self.regressLine.undraw()

    def drawRegressionLine(self, window):
        p1 = Point(self.max_x_win, self.predict(self.max_x_win))
        p2 = Point(self.min_x_win, self.predict(self.min_x_win))
        self.regressLine = Line(p1, p2)
        self.regressLine.draw(window)    
