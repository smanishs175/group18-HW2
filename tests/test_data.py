import unittest
from src.settings import the
from src.data import Data


class TestData(unittest.TestCase):

    def test_data(self):
        d = Data("../data/auto93.csv")
        l = list(d.cols.y)
        for x in l:
            print(x)
        return True

    def test_stats(self):
        data = Data("../data/auto93.csv")
        print('xmid=', data.stats(2, data.cols.x, "mid"))
        print('xdiv=', data.stats(3, data.cols.x, "div"))
        print('ymid=', data.stats(2, data.cols.y, "mid"))
        print('ymid=', data.stats(3, data.cols.y, "div"))
        return True


if __name__ == '__main__':
    unittest.main()
