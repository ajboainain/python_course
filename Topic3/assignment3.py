class Box():

    def __init__(self, length=0, width=0, height=0):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def tsa(self):
        return (2*self.length*self.width) + (2*self.length*self.height) + (2*self.height*self.width)

    def __add__(self, other):
        return self.tsa() + other.tsa()

    def __mul__(self, other):
        return self.tsa() * other.tsa()

    def __LT__(self, other):
        return self.tsa() < other.tsa()

    def __LE__(self, other):
        return self.tsa() <= other.tsa()

    def __GT__(self, other):
        return self.tsa() > other.tsa()

    def __GE__(self, other):
        return self.tsa() >= other.tsa()

    def __EQ__(self, other):
        return self.length == other.length and self.height == other.height and self.width == other.width

    def __NE__(self, other):
        pass


box1 = Box(1, 2, 3)
box2 = Box(4, 5, 6)

print(box1 != box2)
