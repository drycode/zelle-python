def main():
    for i in range (10):
        #receive grade from teacher in number format
        n = (eval(input("Enter a number grade: ")))

        #Use the append method to assign variables to values
        grade = []
        for x in range(0, 60):
            grade.append("F")
        for x in range(60, 70):
            grade.append("D")
        for x in range(70, 80):
            grade.append("C")
        for x in range(80, 90):
            grade.append("B")
        for x in range(90, 300):
            grade.append("A")

        #print results 
        print(grade[n])

main()
