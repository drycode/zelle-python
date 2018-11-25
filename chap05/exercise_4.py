def main():
    print("This program creates acronyms from user input.")

    #get input from user
    title = input("What would you like acronymized? \n")
    
    #initialize output list
    words = []

    #loop for duration of input list split
    for string in title.split():
        #create a temporary variable to store the first
            #letter of each word in upper case
        x = string[0].upper()
        words.append(x)

    #conjoin listed output strings and print
    acro = "".join(words)
    print(acro)

main()
