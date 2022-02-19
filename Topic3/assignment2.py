import math
from sqlite3 import Cursor


class Object3D():

    def volume(self):
        raise NotImplementedError("Please Implement this method")

    def tsa(self):
        raise NotImplementedError("Please Implement this method")


class Box(Object3D):

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def tsa(self):
        return (2*self.length*self.width) + (2*self.length*self.height) + (2*self.height*self.width)


class Cylinder(Object3D):

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * (self.radius**2) * self.height

    def tsa(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)


# box = Box(1, 2, 3)
# cyl = Cylinder(5, 10)

# print("Box volume: ", box.volume())
# print("Box TSA: ", box.tsa())

# print("Cylinder volume: ", cyl.volume())
# print("Cylinder TSA: ", cyl.tsa())
