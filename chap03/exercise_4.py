#Input from user Time Elapsed
#Process 1100 x Time, then divide distance traveled by 5280
#output in miles
def main():
    time_elapsed = eval(input("How long was the time elapsed between flash and the sound of thunder? "))
    miles = 1100 * time_elapsed / 5280
    print("Lightning struck", miles, "miles away.")

main()
