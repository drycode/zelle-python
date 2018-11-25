#stats.py
from math import sqrt

def getNumbers():
    nums = []

    #sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to Quit) >>")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    sum = 0.0
    for num in nums: 
        sum = sum + num
    return sum / len(nums)

def stdDev(nums):
    xbar = mean(nums)
    sumDevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums) - 1))

def meanStdDev(nums):
    xbar = mean(nums)
    std = stdDev(nums)
    return xbar, std


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums [midPos - 1]) / 2
    else:
        median = nums[midPos]
    return median

def main():
    num = (input("Enter a series of numbers, separated by commas: "))
    nums = num.split(',')
    for i in range(len(nums)):
        nums[i] = eval(nums[i])
    print("This program is capable of calculating the mean(Avg), median,(Med)")
    print("and standard deviation(Std) of a set of values.")

    x = 0
    while x != "":
        
        x = (input('Type "Avg", "Med", "Std", or "AvgStd" (<Enter> to exit)>>>  '))
        if x == 'Avg':
            print(mean(nums))
        elif x == 'Med': 
            print(median(nums))
        elif x == 'Std':
            print(stdDev(nums))
        elif x == 'AvgStd':
            print(meanStdDev(nums))
        elif x == '':
            break
        else:
            print("Please try again.")

if __name__ == '__main__': main()
