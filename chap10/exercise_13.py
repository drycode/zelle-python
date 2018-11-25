from face import Face
from graphics import *
from cbutton import CButton

def makeButtons(win):
    wink = CButton(win, Point(16, 17), 1, "Wink")
    meditate = CButton(win, Point(12, 17), 1, "Meditate")
    smile = CButton(win, Point(8, 17), 1, "Smile")
    endGame = CButton(win, Point(4, 17), 1, "Quit")
    wink.activate()
    meditate.activate()
    smile.activate()
    endGame.activate()

    return wink, meditate, smile, endGame
    
def main():
    win = GraphWin("Emoji Jawn", 800, 800)
    win.setCoords(20, 20, 0, 0)
    face = Face(win, Point(10,8), 7)
    wink, meditate, smile, endGame = makeButtons(win)

    pt = win.getMouse()
    while not endGame.clicked(pt):
        if wink.clicked(pt):
            face.wink()
            pt = win.getMouse()
        elif smile.clicked(pt):
            face.smile()
            pt = win.getMouse()
        elif meditate.clicked(pt):
            face.meditate()
            pt = win.getMouse()
        else:
            pt = win.getMouse()
main()
