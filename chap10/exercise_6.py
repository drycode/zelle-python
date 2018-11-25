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

    def addGrade(self, gradePoint, credits):
        self.hours = float(self.hours) + float(credits)
        self.qpoints = self.qpoints + (gradePoint * credits)

    def addLetterGrade(self, letterGrade, credits):
        self.letterGrade = letterGrade

        if self.letterGrade == "A":
            gradePoint = 4
        elif self.letterGrade == "B":
            gradePoint = 3
        elif self.letterGrade == "C":
            gradePoint = 2
        elif self.letterGrade == "D":
            gradePoint = 1
        else:
            gradePoint = 0

        self.hours = float(self.hours) + float(credits)
        self.qpoints = self.qpoints + (gradePoint * credits)

def makeStudent(infoStr):
    #inforStr is a tap-separated line: name hours getQPoints
    #returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    new = makeStudent("Smith, Frank	0	0")
    x = input("Input gradepoint OR letter grade. ")
    y = eval(input("Input credit hours. "))
    if x.isdigit() == True:
        x = eval(x)
        new.addGrade(x, y)
    else:
        new.addLetterGrade(x.upper(), y)
    print(new.getHours(), new.getQPoints())
    print(new.gpa())

main()
