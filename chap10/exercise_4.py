#Three Button Monte
from button import Button
from graphics import GraphWin, Point, Text
from random import random
from time import sleep

def gameplay(click, win, wins, losses):
    #use button.py module to create doors and activate them
    door1 = Button(win, Point(-7.5, -8), 5, 18, "Door 1")
    door2 = Button(win, Point(0, -8), 5, 18, "Door 2")
    door3 = Button(win, Point(7.5, -8), 5, 18, "Door 3")

    door1.activate()
    door2.activate()
    door3.activate()

    #simulate prize behind different doors
    x = random() * 3
    pt1 = pt2 = pt3 = False
    if 0 <= x <1:
        pt1 = True
    elif 1 <= x < 2:
        pt2 = True
    else:
        pt3 = True

    click = win.getMouse()

    #allow user to guess which door prize is behind
    while door1.clicked(click) or door2.clicked(click) or door3.clicked(click):
        if door1.clicked(click):
            if pt1 == True:
                door1.update(win,"Victory!")
                sleep(1)
                wins = wins + 1
            else:
                door1.update(win,"Try Again")
                sleep(1)
                losses = losses + 1
                break
        elif door2.clicked(click):
            if pt2 == True:
                door2.update(win,"Victory!")
                sleep(1)
                wins = wins + 1
            else:
                door2.update(win,"Try Again")
                sleep(1)
                losses = losses + 1
                break
        else:
            if pt3 == True:
                door3.update(win,"Victory!")
                sleep(1)
                wins = wins + 1
            else:
                door3.update(win,"Try Again")
                sleep(1)
                losses = losses + 1
                break
    return click, wins, losses


def printSummary(wins, losses):
    print("Wins: {0:5} Losses: {1:5}".format(wins, losses))

def main():
    win = GraphWin("Three Button Monte", 500, 300)
    win.setCoords(-12, -12, 12, 12)
    win.setBackground("green3")

    #define gameover button and set to active
    gameover = Button(win, Point(9, 10), 3, 3, "Quit")
    gameover.activate()

    direction = Text(Point(0, 10), "Pick a Door")
    direction.draw(win)

    #initialize variables to enter loop
    click = Point(0,0)
    wins = losses = 0
    while not gameover.clicked(click):
        click, wins, losses = gameplay(click, win, wins, losses)

    printSummary(wins, losses)

main()
