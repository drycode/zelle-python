#This program calculates avg word length, counts lines, total characters, and total words 
def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()


    #initialize output list
    numWords = []
    letTotal = 0
    #loop for duration of input list split
    for string in data.split():
        #create a temporary variable to store the first
        #letter of each word
        x = string[0]
        numWords.append(x)
        letTotal = len(string) + letTotal
        wordAvg = letTotal / (len(numWords))
    infile.close()

    infile = open(fname, "r")
    fileLines = infile.readlines()

    lines = []
    for line in fileLines:
        lines.append(line)
    print("There are {0} lines in the file.".format(len(lines)))

    #conjoin listed output strings and print
    print("The avg word length is {0}".format(wordAvg))
    print("The total number of letters is {0}".format(letTotal))
    print("The number of words is {0}".format(len(numWords)))
    infile.close()
main()
