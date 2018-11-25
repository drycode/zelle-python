"""Having trouble moving the face around the screen. Rather than guessing 
until I get it right, I figured it would make sense to get some peer
help understanding the concept of classes as they relate to graphics, 
because I have had similar struggles in previous problems."""

from graphics import *

class GraphicsGroup:
    def __init__(self, anchor):
        self.anchor = anchor
        self.group = []

    def getAnchor(self):
        return self.anchor
    
    def addObject(self, gObject):
        self.group.append(gObject)
    
    # Move the group (and all of it's inhabitants) to a new x/y
    def move(self, dx, dy):
        # Iterate over the objects in self.group,
        # and for each, call object.move(dx, dy)                    
        for graphics_object in self.group:
            graphics_object.move(dx, dy)
    
    def draw(self, win):
        for graphics_object in self.group:
            graphics_object.draw(win)

    def undraw(self):
        for graphics_object in self.group:
            graphics_object.undraw()

def eyes(center, size):
    eyeSize = .15 * size
    eyeOff = size / 3.0
    
    leftEye = Circle(center, eyeSize)
    leftEye.move(-eyeOff, eyeOff)
    rightEye = Circle(center, eyeSize)
    rightEye.move(eyeOff, eyeOff)
    return leftEye, rightEye

def main():
    win = GraphWin("Face or something", 400, 400)
    win.setCoords(0, 0, 10, 10)
    center = Point(5,5)
    face = GraphicsGroup(center)
    head = Circle(face.getAnchor(), 1.2)
    leftEye, rightEye = eyes(face.getAnchor(), 1.2)
    for i in [leftEye, rightEye, head]:
        face.addObject(i)
    
    face.draw(win)
    print(face.getAnchor())
    for i in range(20):
        face.move(.1, .1)
    win.getMouse()

main()