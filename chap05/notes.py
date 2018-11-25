print("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))

#Strings variables can be split into smaller string variables
    #get the date
    dateStr = input("Enter a date (mm/dd/yyy): ")

    #split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

#accumulation loop for Unicode values
    x = 0

    for ch in "zelle":
    	x = int(ord(ch)) + x -96
    print(x)

#for separating a letter
    msg = ""
    for s in "secret".split("e"):
        msg = msg + s
    print(msg)

#for Caesar cipher
    for ch in strExample:
        cipher = (chr(ord(ch)+x))
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
#
