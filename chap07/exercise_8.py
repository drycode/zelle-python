def main():
    cit = eval(input("How many years have you been a U.S. Citizen? "))
    age = eval(input("How old are you? "))
    if cit >= 9:
        if age >= 30:
            print("You are elibible to serve as a U.S. Senator, or a member of the House.")
        elif 30 > age >= 25:
            print("You are eligible to run for the House of Representatives.")
        else:
            print("Sorry, but you are not eligible to serve as a congressional representative.")
    else:
        print("Sorry, but you are not eligible to serve as a congressional representative.")
main()
