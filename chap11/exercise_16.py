from math import sqrt

class StatSet:
    def __init__(self):
        self.stats = []

    def addNumber(self, x):
        self.stats.append(x)

    def mean(self):
        sum = 0.0
        for num in self.stats: 
            sum = sum + num
        return sum / self.count()

    def median(self):
        self.stats.sort()
        size = len(self.stats)
        midPos = size // 2
        if size % 2 == 0:
            median = (self.stats[midPos] + self.stats[midPos - 1]) / 2
        else:
            median = self.stats[midPos]
        return median

    def stdDev(self):
        xbar = self.mean()
        sumDevSq = 0.0
        for num in self.stats:
            dev = xbar - num
            sumDevSq = sumDevSq + dev * dev
        return sqrt(sumDevSq/(len(self.stats) - 1))

    def count(self):
        return len(self.stats)

    def min(self):
        self.stats.sort()
        return self.stats[0]

    def max(self):
        self.stats.sort(reverse=True)
        return self.stats[0]

def main():
    data = StatSet()
    for i in range(12):
        data.addNumber(i * 3/2)
    print(data.count())
    print(data.mean())
    print(data.median())
    print(data.stdDev())
    print(data.min())
    print(data.max())
main()
    