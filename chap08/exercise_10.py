#This program computes the fuel efficiency of a multi-leg journey
def MPG(odom, infile):
    count = 0

    #get information about a series of legs
    totGas = 0
    totDistance = 0
       
    for leg in infile.readlines():
        leg = str(leg)
        while leg != "\n":
            #current odometer and amount of gas used separated by space
            try:
                newodom, gas = leg.split(" ")
                newodom = eval(newodom)
                gas = eval(gas)

                count = count + 1

                #distance traveled per leg
                distance = newodom - odom
                
                #total distance
                totDistance = distance + totDistance

                #compute MPG for leg
                legMPG = distance/gas

                #set new odometer reading
                odom = newodom

                print("On leg {0}, you got {1}/gal.".format(count, round(legMPG, 2)))

                #add values to trip total
                totGas = totGas + gas
                totMPG = totDistance / totGas
                break

            except ValueError:
                break
    
    return totMPG

def main():
#Prompt the user for the starting odometer
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    odom = int(input("What is your current odometer reading: "))
    totMPG = MPG(odom, infile)

#print out miles/gal on each leg and the total MPG for the trip
    print("On whole trip, you averaged {0}/gal.".format(round(totMPG, 2)))
main()
