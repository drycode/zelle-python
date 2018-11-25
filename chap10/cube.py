#cube.py

class Cube:
    """This class represents a geometric solid cube.
    It will return side length, surface area, and volume
    using getSideLength(), surfaceArea(), and volume()."""

    def __init__(self, side):
        self.side = side

    def getSideLength(self):
        return self.side

    def surfaceArea(self):
        self.surfaceArea = 6 * self.side ** 2
        return self.surfaceArea

    def volume(self):
        self.volume = self.side ** 3
        return self.volume
