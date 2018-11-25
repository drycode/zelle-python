def main():
    #x = input(eval("Please report speed: "))
    #y = input(eval("What is the reported speed limit?"))
    x = -34
    y = 65
    t = x - y
    if t >= 0:
        fine = (t // 5) * 5 + 50
        if x >= 90:
            fine = fine + 200
        print("You owe ${0}.".format(fine))
    elif t < 0:
        print("You have not committed a speed violation.")
    else:
        print("Check the speed limit or reported speed.")
main()
