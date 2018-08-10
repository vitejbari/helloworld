import unittest
from cal import Mathematics

class TestMethods(unittest.TestCase):
    def test_assert(self):
        self.assertEqual(Cal.add(),x+y)
    def test_assert1(self):
        self.assertEqual(Cal.subt(),x-y)
    def test_assert2(self):
        self.assertEqual(Cal.multiply(),x*y)
    def test_assert3(self):
        self.assertEqual(Cal.div(),x/y)

x = 123456789
y = 123
Cal = Mathematics(x,y)

"""print(Cal.add())
print(Cal.subt())
print(Cal.multiply())
print(Cal.div())"""

if __name__ == '__main__':
    unittest.main()
