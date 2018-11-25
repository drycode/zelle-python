from gpa import Student
from graphics import *
from button import Button

def makeStudent(infoStr):
    #inforStr is a tap-separated line: name hours getQPoints
    #returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    #students is a list of Student object
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file = outfile)
    outfile.close()

def sort(filename, x, m):
    data = readStudents(filename)
    while True:
        if x == 'GPA':
            data.sort(key=Student.gpa)
            s = "_(GPA)"
            if m == "D":
                data.reverse()
            break
        elif x == 'name': 
            data.sort(key=Student.getName)
            s = "_(name)"
            if m == "D":
                data.reverse()
            break 
        elif x == 'credits':
            data.sort(key=Student.getQPoints)
            s = "_(credits)"
            if m == "D":
                data.reverse()
            break
        else:
            print("Please try again.")
        
    #filename = input("enter a name for the outputfile: ")
    filename = "gpa" + s + ".txt"
    return filename, data

def main():
    #infile = input("Enter the name of the data file: ")
    infile = 'gpa1.txt'
    
    #Open Graphics Window
    win = GraphWin("Arrange Student File", 800, 800)
    win.setCoords(0, 0, 5, 6)

    message = Text(Point(2.5,3), "This program sorts student grade information by GPA, name, or credits.\n Select the sorting method you would like.")
    message.draw(win)

    #Create Buttons for GPA, Name, and Credits
    bSpecs = [(1,2,"GPA"), (2,2,"Name"), (3,2,"Credits"), (4,2,"Quit")]
    buttons = []
    for (cx, cy, label) in bSpecs:
        buttons.append(Button(win, Point(cx,cy), .75, .75, label))
    
    #....activate
    for b in buttons:
        b.activate()
    
    while True:
        click = win.getMouse()
        
        #return clicked for each button
        for b in buttons:
            if b.clicked(click):
                label = b.getLabel()
        while label != "Quit":
            if label == "GPA":
                x = "GPA"
                m = "D"
                break
            elif label == "Name":
                x = "name"
                m = "A"
                break
            elif label == "Credits":
                x = "credits"
                m = "D"
                break
            elif label == "Quit":
                break
            else:
                message.setText("Please try again.")
                click = win.getMouse()
        #call sort function, which should return filename
        outfile, data = sort(infile, x, m)
        writeStudents(data, outfile)
        outmessage = "The file has been printed to "+ outfile
        message.setText(outmessage)
        if label == "Quit":
            break
    

if __name__ == '__main__': main()



