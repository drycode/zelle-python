def squareEach(nums):
    for x in range (len(nums)):
        nums[x] = nums[x] ** 2        
    return(nums)
def test():
    list = [1,2,3,4,5]
    y = squareEach(list)
    print(y)
test()
