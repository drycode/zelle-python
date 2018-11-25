import math as m
from tracker import Tracker
from projectile import Projectile
from graphics import *

def main():
    win = GraphWin("Projectile Tracker", 600, 600)
    win.setCoords(0, 0, 1400, 1400)
    missile = Projectile(45, 100, 0)
    tracker = Tracker(win, missile, 1400)
    while missile.getY() >= 0:
        missile.update(.05)
        dx = missile.getX()
        dy = missile.getY()
        tracker.move(dx, dy)
        print("{}:{}".format(missile.getX(), missile.getY()))


main()