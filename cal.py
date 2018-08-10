#import unittest
class Mathematics:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subt(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y


x = 13
y = 11
Cal = Mathematics(x,y)

"""print(Cal.add())
print(Cal.subt())
print(Cal.multiply())
print(Cal.div())"""

