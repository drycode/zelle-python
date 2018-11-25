def main():
    #get time in hours and minutes and convert into float of hours
        #time = input("Please enter the time eg. (hh:mm): ")
    starTime = '9:15'
    endTime = '23:15'

    starMin = eval(starTime[-2:len(starTime)])
    starHr = eval(starTime[:len(starTime)-3])
    endMin = eval(endTime[-2:len(endTime)])
    endHr = eval(endTime[:len(endTime)-3])

    starTime = starHr + 1 / (60/starMin)
    endTime = endHr + 1 / (60/endMin)

    time = endTime - starTime
    if endTime < 21:
        bill = time * 2.50
    else:
        x = endTime - 21
        bill = (time - x) * 2.50 + (x * 1.75)
    print("${0}".format(round(bill, 2)))
main()
