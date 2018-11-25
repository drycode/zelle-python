def main():
    #get the date
    day, month, year = eval(input("Enter a day, month, and year in numbers: "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

    monthStr = months[month-1]
    date2 = monthStr+" " + str(day) + ", " + str(year)

    #output
    print("The converted date is", date1, "or", date2+".")

main()
