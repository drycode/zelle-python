#tracker.py
from graphics import *

class Tracker:
    def __init__(self, window, objToTrack, max_min_X_coords):
        #window is a graphWin and objToTrack is an object whose
        #position is to be shown in the window. 
        self.window = window
        # objToTrack is
        #an object that has getX() and getY() methods that
        #report its current position.
        self.objToTrack = objToTrack
        #Creates a Tracker object and draws a circle in window
        #at the current position of objToTrack
        xpos = objToTrack.getX()
        ypos = objToTrack.getY()
        self.center = Point(xpos, ypos)
        self.size = max_min_X_coords/100
        self.tracker = Circle(self.center, self.size)
        

    def initializeTracker(self):
        self.tracker = Circle(self.center, self.size)
        self.tracker.setFill("black")
        self.tracker.draw(self.window)

    def move(self, dx, dy):
        #Moves the circle in the window to the current position
        #   of the object being tracked
        self.tracker.undraw()
        self.center = Point(dx, dy)
        self.initializeTracker()

    def getPosition(self):
        return self.center