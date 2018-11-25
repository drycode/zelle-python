print("This Program ilustrates a chaotic function")
n = eval(input("How many numbers should I print? "))
x = eval(input("Enter a value between 0 and 1: "))
for i in range(n):
    x = 3.9 * x * (1-x)
    print(x)
