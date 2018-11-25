#word count
def main():
    text = input("Input: \n")

    #initialize output list
    word_len = []

    #loop for duration of input list split
    for string in text.split():
        #create a temporary variable to store the first
        #letter of each word
        x = string[0]
        word_len.append(x)

    #conjoin listed output strings and print
    print(len(word_len))

main()
