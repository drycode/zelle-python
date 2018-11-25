def main():
    x = eval(input("What is the number grade? "))
    if x == 5:
        print('A')
    elif x == 4:
        print('B')
    elif x == 3:
        print('C')
    elif x == 2:
        print('D')
    elif x == 1:
        print('F')
    elif x == 0:
        print('F')
    else:
        print('Please enter an integer between 0 and 5')
main()
