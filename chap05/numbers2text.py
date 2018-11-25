def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents. \n")

    #Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    #Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)              #convert digits to a number
        message = message + chr(codeNum)    #concatentate character to message

    print("\nThe decoded message is:", message)

main()
