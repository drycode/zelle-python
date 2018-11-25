#this program draws a quiz score histogram
from graphics import *

def main():
    #read file from disk
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    #create 11 items in List as accumulator variable for scores 0-10
    scores = [0,0,0,0,0,0,0,0,0,0,0]

    #for counting total students
    students = 0

    #loop through each line and use list index as counter for
    #each scores number
    for line in infile.readlines():
        scores[int(line)] = scores[int(line)]+1
        students = students + 1

    #draw a bar graph to represent each occurance of possible scores
    height = max(scores)

    # 1 Coord = 10px
    # each score bar height increse 10px too.
    win = GraphWin('Quiz Histogram', 640, 480)
    win.setCoords(0, 0, 35, height * 1.5)

    #show total students
    students = 'Total Students: '+str(students)

    totalStudent = Text(Point(8,.1 * height), students)
    totalStudent.draw(win)

    pos = 2
    hgt = .2 * height
    for i in range(11):
        bar = Rectangle(Point(pos, hgt),Point(pos + 2, scores[i] + hgt))
        bar.setFill('red')
        bar.draw(win)

        pos = pos+3

    #bar number 0-10
    position = 3
    hgt = .1 * height +  1
    for i in range(11):
        Text(Point(position, hgt), i).draw(win)
        position = position + 3

    win.getMouse()
    win.close()


    infile.close()

main()
