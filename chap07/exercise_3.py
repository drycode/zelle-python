def main():
    #x = eval(input("What is the number grade? "))
    x = 84
    if x >= 90:
        print('A')
    elif 90 > x >= 80:
        print('B')
    elif 80 > x >= 70:
        print('C')
    elif 70 > x >= 60:
        print('D')
    elif 60 > x:
        print('F')
    else:
        print('Please enter an integer between 0 and 100')
main()
