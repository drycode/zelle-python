# Get into the habit of using more descriptive variable names.
# It will make the lives of whoever has to read this code easier (yourself included)
def windchill(temperature, windspeed):
    if 50 >= windspeed >= 3:
        windchill = 35.74 + (0.6215 * temperature) - (35.75 * (windspeed ** 0.16)) + (0.4275 * temperature) * (windspeed ** 0.16)
    else:
        windchill = 0
    return windchill

def generateWindchillTable(rows):
  # Extra credit - find a way to ensure the rows argument is a number, and not a string or a boolean (the for loop will fail if it isn't)
    try:
        if rows == True or rows == False or rows == None:
            print("Use a number not a boolean")
        else:
            for i in range (rows):
                print("{0:2} {1:>8.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f}".format(i*5,windchill(-20, i*5), windchill(-10, i*5), windchill(0, i*5), windchill(10, i*5), windchill(20, i*5), windchill(30, i*5), windchill(40, i*5), windchill(50, i*5)))
    except NameError as rows:
        print("rows must be a number!")
    except TypeError as rows:
        print("rows must be a number!")
    except SyntaxError:
        print("rows must be a number!")

def main():

    print("{0:>}".format("Table of Windchill Values"))
    print("{0:>11} {1:6} {2:6} {3:6} {4:>6} {5:6} {6:6} {7:6}".format(-20, -10, 0, 10, 20, 30, 40, 50))
    print("")
    generateWindchillTable(11)

main()
