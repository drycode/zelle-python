
def ants():
    num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    rhyme = ['suck his thumb','tie his shoe','take a pee', 'shut the door','call the hive','pick up sticks', 'look to heaven','make a date', 'get outta line', 'sing it again']
    for i in range (10):
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(num[i])))
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(num[i])))
        print("The ants go marching {0} by {0},".format(str(num[i])))
        print("The little one stops to {0},".format(str(rhyme[i])))
        print("And they all go marching down...")
        print("Into the ground...")
        print("To get out...")
        print("Of the rain.")
        print("Boom! Boom! Boom!")
        print()
def main():
    ants()
main()
