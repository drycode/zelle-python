def main():

#Get plaintext(p_text) and key(x) from the user
    p_text = input("Enter the message you'd like encrypted.\n")
    key = eval(input("What's the key? : "))

    p_text = p_text.lower()
    
#Create string of letters
    table = "abcdefghijklmnopqrstuvwxyz"

#Convert plaintext to ciphertext(c_text) using cipher loop
    c_text = ""
    for ch in p_text:
        c_text = c_text + (table[((ord(ch)) - 97) + key % 52])

    print("Your encoded message is {0}.".format(c_text))

main()
