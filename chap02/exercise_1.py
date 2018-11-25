def main():
    print("Welcome! This program will kindly convert", "\n", "your degrees Celsius into Fahrenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = (celsius - 32) * 5/9
    print("The temperature is ", fahrenheit, "degrees Fahrenheit.")

main()
