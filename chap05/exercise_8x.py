#improved Caesar cipher
def main():

#Get plaintext(p_text) and key(x) from the user
    p_text = input("Enter the message you'd like encrypted.\n")
    key = eval(input("What's the key? : "))

#Create string of letters
    table = "abcdefghijklmnopqrstuvwxyz"

    #initialize output list
    c_text = []

    #loop for duration of input list split
    for c_string in p_text.split(" "):
        #create a temporary variable to store each c_text word (c_string)
        #Convert plaintext to ciphertext(c_text) using cipher loop
        x = c_string + (table[((ord(ch)) - 97) + key % 52])
        #compile new list c_text
        c_text.append(c_string)
    print(c_text)
#Convert plaintext to ciphertext(c_text) using cipher loop
    c_text = ""
    for ch in p_text:
        c_text = c_text + (table[((ord(ch)) - 97) + key % 52])

    print("Your encoded message is {0}.".format(c_text))

main()
