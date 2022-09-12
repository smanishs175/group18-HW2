import unittest
from src.settings import the
from src.readCSV import *
from src.utils import *

class TestCsv(unittest.TestCase):

    def test_csv(self):
        '''Test case for csv function'''
        self.n = 0
        Csv(src="../data/auto93.csv", fun=self.func_test)
        return True
    
    def func_test(self, row):
        self.n = self.n + 1
        if self.n > 10:
            return 
        return oo(row)


if __name__ == "__main__":
  unittest.main()
