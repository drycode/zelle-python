import math as m

def main():
    H, C, O = eval(input("Enter the number of Hydrogen, Carbon, and Oxygen atoms separated by commas: "))
    mol_weight = H * 1.0079 + C * 12.011 + O * 15.9994
    print("The molecular weight of the hydrocarbon is", mol_weight, "g/mol")

main()
