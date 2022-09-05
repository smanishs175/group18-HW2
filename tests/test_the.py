import unittest
from src.settings import the
from src.utils import *

class TestThe(unittest.TestCase):

    def test_the(self):
        '''Test case for the function'''
        oo(the())
        return True


if __name__ == "__main__":
  unittest.main()