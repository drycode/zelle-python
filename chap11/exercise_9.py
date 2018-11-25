from gpa import Student

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def makeStudent(infoStr):
    #inforStr is a tap-separated line: name hours getQPoints
    #returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def writeStudents(students, filename):
    #students is a list of Student object
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s[1], s[2], s[3]), file = outfile)
    outfile.close()

def sort(students):
    newData = []
    for i in range(len(students)):
        x = (students[i].gpa(), students[i].getName(), students[i].getHours(), students[i].getQPoints())
        newData.append(x)
        newData.sort()
        newData.reverse()

    return newData

def main():
    print("This program sorts student grade information by GPA")
    #filename = input("Enter the name of the data file: ")
    filename = "gpa1.txt"
    data = readStudents(filename)
    data = sort(data)
    
    filename = "gpa_(sortfast).txt"
    writeStudents(data, filename)    
    
    
    

if __name__ == '__main__': main()



