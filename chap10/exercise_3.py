#Three Button Monte
from button import Button
from graphics import GraphWin, Point, Text
from random import random

def main():
    win = GraphWin("Three Button Monte", 500, 300)
    win.setCoords(-12, -12, 12, 12)
    win.setBackground("green3")

    door1 = Button(win, Point(-7.5, -8), 5, 18, "Door 1")
    door2 = Button(win, Point(0, -8), 5, 18, "Door 2")
    door3 = Button(win, Point(7.5, -8), 5, 18, "Door 3")
    direction = Text(Point(0, 10), "Pick a Door")
    direction.draw(win)
    x = random() * 3
    pt1 = pt2 = pt3 = False
    if 0 <= x <1:
        pt1 = True
    elif 1 <= x < 2:
        pt2 = True
    else:
        pt3 = True

    door1.activate()
    door2.activate()
    door3.activate()
    click = win.getMouse()

    while door1.clicked(click) or door2.clicked(click) or door3.clicked(click):
        if door1.clicked(click):
            if pt1 == True:
                door1.update(win,"Victory!")
            else:
                if door2.clicked(click):
                    door2.update(win,"Correct Door.")
                    click = win.getMouse()
                else:
                    door3.update(win,"Correct door.")
                    click = win.getMouse()
        elif door2.clicked(click):
            if pt2 == True:
                door2.update(win,"Victory!")
            else:
                if door3.clicked(click):
                    door3.update(win,"Correct Door.")
                    click = win.getMouse()
                else:
                    door1.update(win,"Correct door.")
                    click = win.getMouse()
        else:
            if pt3 == True:
                door3.update(win,"Victory!")
            else:
                if door2.clicked(click):
                    door2.update(win,"Correct Door.")
                    click = win.getMouse()
                else:
                    door1.update(win,"Correct door.")
                    click = win.getMouse()

    win.getMouse()
main()
