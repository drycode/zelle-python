def acronym(phrase):
    words = []
    #loop for duration of input list split
    for string in phrase.split():
        #create a temporary variable to store the first
            #letter of each word in upper case
        x = string[0].upper()
        words.append(x)

    #conjoin listed output strings and print
    acro = "".join(words)
    return acro
def main():
    phrase = input("What would you like acronymized? \n")
    x = acronym(phrase)
    print(x)
main()
