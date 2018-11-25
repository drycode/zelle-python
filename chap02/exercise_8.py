def main():
    print("Welcome! This program will kindly convert", "\n", "your degrees Fahrenheit into Celsius.")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature is ", celsius, "degrees Fahrenheit.")

main()
