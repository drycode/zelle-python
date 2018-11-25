import math as m
from tracker import Tracker
from projectile import Projectile
from graphics import *
from button import Button

def main():
    win = GraphWin("Projectile Tracker", 600, 600)
    win.setCoords(0, 0, 1400, 1400)
    missile = Projectile(45, 100, 0)
    tracker = Tracker(win, missile, 1400)
    target = Button(win, Point(1021, 70), 140, 140, "x")
    target.activate()
    click = Point(missile.getX(), missile.getY())
    while not target.clicked(click):
        missile.update(.05)
        dx = missile.getX()
        dy = missile.getY()
        tracker.move(dx, dy)
        click = tracker.getPosition()
        print(click.getX(), click.getY())
        if dy <= 0:
            angle = eval(input("Angle: "))
            velocity = eval(input("Velocity: "))
            height = eval(input("Initial Height: "))
            missile = Projectile(angle, velocity, height)
    
main()