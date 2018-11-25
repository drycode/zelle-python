#This program plots student exam scores on a horizontal bar chart
#open student_test.txt
from graphics import *
def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    #grab number of students and assign to numStud
    numStud = int(infile.readline())
    
    #grab name and grade and assign to lists studName and grade
    studName = []
    grade = []
    lines = []
    for line in infile.readlines():
        x, y = line.split(": ")
        #strip \n
        y = y[0:-1]
        studName.append(x)
        grade.append(y)

    print(studName)
    print(grade)
    
#initialize graphWin of size 400, (100 x numStud)
    win = GraphWin("Student Grade Chart", 400, 50 * numStud)

    #setCoords: -10, 0, 100, (10 x (numStud + 2))
    win.setCoords(-30, (10 * numStud + 2), 120, 0)

    #draw text studName
    for i in range (numStud):
        s = studName[i].rjust(10)
        Text(Point(-20, 15 + numStud * .8 * i), s).draw(win)
    #draw Rectangle and clone
    for i in range (numStud):
        r = Rectangle(Point(0, 13 + numStud * .8 *i), Point(grade[i], 17 + numStud * .8 * i))
        r.draw(win)
#close file
    infile.close()
main()
