def happy():
    print("Happy Birthday to You!")

def sing(person):
    happy()
    happy()
    print("Happy Birthday, dear", person + ".")
    happy()

def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")

main()
