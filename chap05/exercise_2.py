def main():
    #receive grade from teacher in number format
    n = eval(input("Enter a grade with no separation. "))

    #create a list that associates numbers 5-0 with grades A-F
    grade = ["F", "F", "D", "C", "B", "A"]

    #print results using string formatting
    print(grade[n])

main()
