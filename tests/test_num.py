import unittest
from src.settings import the
from src.num import Num

class TestNum(unittest.TestCase):

    def test_num(self):
        '''Test case for div function'''
        num = Num(0, "random")
        for i in range(1, 101):
            num.add(i)
        mid, div = num.mid(), num.div()
        print(mid, div, num.n)
        self.assertTrue(50 <= mid and mid <= 52 and 30.5 < div and div < 32)

if __name__ == "__main__":
  unittest.main()
