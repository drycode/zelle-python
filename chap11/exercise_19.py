"""This set class represents a classical set."""
class Set:
    def __init__(self, elements):
        self.set = []
        for i in elements:
            self.set.append(i)

    def addElement(self, x):
        self.set.append(x)

    def deleteElement(self, x):
        if self.member(x):
            self.set.remove(x)
    
    def member(self, x):
        if x in self.set:
            return True
        else:
            return False
    
    def intersection(self, set2):
        intersection = []
        for x in set2:
            if x in (set2 and self.set):
                intersection.append(x)
        return intersection

    def union(self, set2):
        for x in set2:
            self.set.append(x)
    
    def subtract(self, set2):
        for x in set2:
            while x in self.set:
                self.set.remove(x)
        
    def getSet(self):
        return self.set

def main():
    list1 = ['cat', 'dog', 'fish', 'mouse', 'banana']
    test = Set(list1)
    test.addElement('small')
    test.deleteElement('dog')
    
    list2 = ['flat', 'cat', 'rectangle', 'banana', 'dog', 'mouse', 'lemon']
    list3 = ['cat', 'dog', 'mouse', 'fish']
    intersect = test.intersection(list2)
    test.union(list2)
    test.subtract(list3)

    print(test.getSet())
    print(intersect)


main()