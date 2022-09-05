import unittest
from CSC510_43.src.main import the
from CSC510_43.src.num import Num

class TestNum(unittest.TestCase):

    def test_div(self):
        '''Test case for div function'''
        num = Num()
        the['nums'] = 512
        for i in range(1, 101):
            num.add(i)
        std = num.div()
        self.assertTrue(28 < std < 30)

    def test_mid(self):
        '''Test case for mid function'''
        num = Num()
        the['nums'] = 512
        for i in range(1, 101):
            num.add(i)
        median = num.mid()
        self.assertTrue(50 <= median <= 52)

if __name__ == "__main__":
  unittest.main()
