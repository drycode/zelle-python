#msdie.py
#   Class definition for an n-sided die.
from random import randrange

class Person:
    def __init__(self, name, age):
        this.name = name
        this.age = age

class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

def main():
    die1 = MSDie(12)
    die2 = MSDie(100)
    die1.roll()
    print(die1.getValue())

main()
