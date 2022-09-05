import unittest
from group18-HW2 import the
from group18-HW2 import Num

class TestBigNum(unittest.TestCase):

    def test_storage(self):
        '''Test case for storage'''
        num = Num()
        the['nums'] = 32
        for i in range(1, 1001):
            num.add(i)
        self.assertEqual(32, len(num.has))

if __name__ == "__main__":
  unittest.main()