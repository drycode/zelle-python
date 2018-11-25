def sumList(nums):
    y = 0
    for x in range (len(nums)):
        y = nums[x] + y
    return(y)
def test():
    list = [1,2,3,4,5]
    z = sumList(list)
    print(z)
test()
