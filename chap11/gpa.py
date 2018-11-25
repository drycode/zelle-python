#gpa.py
#   Program to find student with highest GPA

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

def makeStudent(infoStr):
    #inforStr is a tap-separated line: name hours getQPoints
    #returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    #open the input file for reading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')

    #set best to the record for the first student in the file
    best = makeStudent(infile.readline())

    #process subsequent lines of the file
    for line in infile:
        #turn the line into a student record
        s = makeStudent(line)
        #if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    #print information about the best student
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())

if __name__ == '__main__':
    main()
