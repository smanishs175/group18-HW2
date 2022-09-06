import unittest
from src.sym import Sym

class TestSym(unittest.TestCase):

    def test_sym(self):
        '''Test case for div function'''
        arr = ["a", "a", "a", "a", "b", "b", "c"]
        sym = Sym(0, "random")
        for index, value in enumerate(arr):
            sym.add(value)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        self.assertTrue(mode == "a" and 1.37 <= entropy <= 1.38)

if __name__ == "_main_":
  unittest.main()