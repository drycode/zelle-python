#word count
def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()

    #initialize output list
    numWords = []

    #loop for duration of input list split
    for string in data.split():
        #create a temporary variable to store the first
        #letter of each word
        x = string[0]
        numWords.append(x)

    letTotal = 0
    for string in data.split():
        letTotal = len(string) + letTotal
        wordAvg = letTotal / (len(numWords))
    #conjoin listed output strings and print
    print("The Avg word lenth is {0}".format(wordAvg))
    print("The total number of letters is {0}".format(letTotal))
    print("The number of words is {0}".format(len(numWords)))
main()
