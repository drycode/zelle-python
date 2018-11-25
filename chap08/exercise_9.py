#This program computes the fuel efficiency of a multi-leg journey
def MPG(start_odom):
    count = 0

    #get information about a series of legs
    leg = 0
    totGas = 0
    while leg != "\n":
        #current odometer and amount of gas used separated by space
        leg = input("Enter the current odometer and amount of gas (gallons), \nseparated by a space (<Enter> to quit)>> ")
        try:
            newodom, gas = leg.split(" ")
            newodom = eval(newodom)
            gas = eval(gas)

            count = count + 1

            #distance traveled per leg
            distance = newodom - odom
            #compute MPG for leg
            legMPG = distance/gas

            #set new odometer reading
            odom = newodom

            print("On leg {0}, you got {1}/gal.".format(count, round(legMPG, 2)))

            #add values to trip total
            totGas = totGas / gas
        except ValueError:
            break
    return totGas, distance

def main():
#Prompt the user for the starting odometer
    odom = int(input("What is your current odometer reading: "))
    totGas, distance = MPG(odom)

#print out miles/gal on each leg and the total MPG for the trip
    totMPG = distance + totGas
    print("On whole trip, you averaged {1}/gal.".format(count, round(totMPG, 2)))
main()
