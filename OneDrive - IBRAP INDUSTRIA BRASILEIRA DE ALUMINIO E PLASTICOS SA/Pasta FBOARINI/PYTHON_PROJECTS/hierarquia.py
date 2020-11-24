import random


class MyList(list):
    def choice(self):
        return random.choice(self)

class Point:

    def __init__(self, x = 0,y = 0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x,self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

p = Point()
p.setx(9)
p.sety(4)

m = MyList([2,8,9,7,6,3])

print(p)
print(m)