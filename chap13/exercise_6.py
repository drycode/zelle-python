class BaseConversion:
    def __init__(self, num, base):
        self.list = []
        self.num = num
        self.base = base
        self.makeList()
    
    def makeList(self):
        digit = self.num % self.base
        self.list.append(digit)
        self.num = self.num // self.base

        if self.num < self.base:
            digit = self.num
            self.num = 0
            self.list.append(digit)
        else:
            self.makeList()

    def getDigits(self):
        self.list.reverse()
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        newlist = []
        for num in self.list:
            num = digits[num]
            newlist.append(num)
        str1 = ' '.join(newlist)
        return str1

list = BaseConversion(153, 10)
newlist = list.getDigits()

print(newlist)
