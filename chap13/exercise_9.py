from graphics import GraphWin, Point, Line
from math import pi, cos, sin, sqrt

def C_Curve(Turtle, length, degree):
    if degree == 0:
        Turtle.draw(length)
    else:
        length1 = length/(sqrt(2))
        degree1 = degree - 1
        Turtle.turn(45)
        C_Curve(Turtle, length1, degree1)
        Turtle.turn(-90) 
        C_Curve(Turtle, length1, degree1)
        Turtle.turn(45)
    
class Turtle:
    def __init__(self, point, direction, window):
        self.location = point
        self.direction = direction
        self.win = window
    
    def moveTo(self, newpoint):
        self.location = newpoint
    
    def _moveTo(self, length):
        dx = length * cos(self.direction)
        dy = length * sin(self.direction)
        x = self.location.getX()
        y = self.location.getY()
        x += dx
        y += dy
        newpoint = Point(x, y)
        return self.moveTo(newpoint)
    
    def draw(self, length):
        oldLocation = self.location
        self._moveTo(length)
        path = Line(oldLocation, self.location)
        path.draw(self.win)
    
    def turn(self, direction):
        self.direction += direction * pi / 180


def main():
    length = 300
    degree = 15
    win = GraphWin("C_Curve Snowflake", 800, 800)
    dir = pi / 2 
    turtle = Turtle(Point(475, 225), dir, win)
    C_Curve(turtle, length, degree)
    win.getMouse()
main()