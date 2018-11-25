def main():

#Get plaintext(p_text) and key(x) from the user
    p_text = input("Enter the message you'd like encrypted.\n")
    key = eval(input("What's the key? : "))

#Create string from list 
    #p_text = "".join(inputText)
   
#Convert plaintext to ciphertext(c_text) using cipher loop
    c_text = ""
    for ch in p_text:
        c_text = c_text + (chr(ord(ch) + key))

    print("Your encoded message is {0}.".format(c_text))

main()
