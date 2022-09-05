import unittest
from src.settings import the
from src.num import Num

class TestBigNum(unittest.TestCase):

    def test_storage(self):
        '''Test case for storage'''
        theObj = the()
        theObj.nums = 32
        num = Num(0, "pbrr", theObj)
        for i in range(1, 1001):
            num.add(i)
        self.assertEqual(32, len(num._has))

if __name__ == "__main__":
  unittest.main()