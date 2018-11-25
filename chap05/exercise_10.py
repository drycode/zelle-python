#word count
def main():
    text = input("Input: \n")

    #initialize output list
    numWords = []

    #loop for duration of input list split
    for string in text.split():
        #create a temporary variable to store the first
        #letter of each word
        x = string[0]
        numWords.append(x)

    letTotal = 0
    for string in text.split():
        letTotal = len(string) + letTotal
        wordAvg = letTotal / (len(numWords))
    #conjoin listed output strings and print
    print(wordAvg)

main()
