def BMI(weight, height):
    BMI = (weight * 720) / (height ** 2)
    return BMI
def main():
    x, y = eval(input("What is your weight (in pounds) and height (in inches)?"))
    bmi = BMI(x, y)

    if 19 <= bmi <= 25:
        print("You are within the arbitrary healthy range.")
    elif bmi < 19:
        print("You are below the arbitrary healthy range.")
    elif bmi > 25:
        print("You are above the arbitrary healthy range.")
    else:
        print("Please enter a valid height and weight")
    #try?
main()
