from graphics import *

def face(center, size, window):

    x1 = center.getX()
    y1 = center.getY()
    p1 = Point(x1-(.7 * size), y1 - size)
    p2 = Point(x1+(.7 * size), y1 + size)
                     
    head = Oval(p1, p2)
    head.draw(window)

    lc = Point(x1 - .2 * size, y1 + .6 * size)
    rc = Point(x1 + .2 * size, y1 + .6 * size)

    leftEye = Circle(lc, .13 * size)
    leftEye.draw(window)

    rightEye = Circle(rc, .13 * size)
    #rightEye.move(2 * (x1 + .2 *size), 0)
    rightEye.draw(window)

    m1 = Point(x1 - .3 * size, y1 - .5 * size)
    m2 = Point(x1 + .3 * size, y1 - .25 * size)
    m3 = Point(x1 + .3 * size, y1 - .5 * size)
    
    mouth = Rectangle(m1, m2)
    mouth.draw(window)

    leftLip = Line(m1, Point(x1- .3 * size, y1 - .25 * size))
    mLeftCent = leftLip.getCenter()
    
    mLCx = mLeftCent.getX()
    mLCy = mLeftCent.getY()

    mRightCent = Point(x1 + .3 * size, mLCy)
    
    lip = Line(mLeftCent, mRightCent)
    lip.draw(window)

    m1x = m1.getX()
    m3x = m3.getX()
    m1y = m1.getY()
    m2y = m2.getY()
    
    t = m1x - m3x
    t1 = Point(m1x - (1/8 * t), m2y)
    teeth = Rectangle(m1, t1) 
    teeth.draw(window)

    
    for i in range (7):
        t2 = teeth.clone()
        t2.move(-i * (1/8 * t), 0)
        t2.draw(window)

   
def main():
    window = GraphWin('Smile!', 800,800)
    window.setCoords(0, 0, 20, 20)
    face(Point(0,0), 5, window)
    face(Point(0,0), 9, window)
    face(Point(0,0), 13, window)
    face(Point(0,0), 17, window)
    
main()
