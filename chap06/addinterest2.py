def addInterest(balance, rate):
    newBalance = balance * (1 + .01 * rate)
    return newBalance

def test():
    amount = 1000
    rate = 5
    amount = addInterest(amount, rate)
    print(amount)

test()
