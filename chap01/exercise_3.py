print("This Program ilustrates a chaotic function")
x = eval(input("Enter Number"))
for i in range(10):
    x = 2.0 * x * (1-x)
    print(x)
