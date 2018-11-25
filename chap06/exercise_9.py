def grade(score):
    grades = []
    for x in range(0, 60):
        grades.append("F")
    for x in range(60, 70):
        grades.append("D")
    for x in range(70, 80):
        grades.append("C")
    for x in range(80, 90):
        grades.append("B")
    for x in range(90, 100):
        grades.append("A")
    return grades[score]
def main():
    n = (eval(input("Enter a number grade: ")))
    x = grade(n)
    print(x)
main()
