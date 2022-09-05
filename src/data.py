
from settings import the
from src.readCSV import *
from src.utils import push, rnd
from src.cols import Cols
from src.row import Row

class Data:
    
    #Data:new function
    def __init__(self, src, theObj=the()):
        self.rows = {}
        self.cols = None
        if isinstance(src, str):
            Csv(src=src, sep = theObj.separator, fun=lambda x: self.add(x))
        else:
            print(type(src))
            for _, row in src.items():
                self.add(row)

    #Data:add function
    def add(self, row):
        if not self.cols:
            self.cols = Cols(row)
        else:
            row = push(self.rows, Row(row))
            for col in list(self.cols.x.values()) + list(self.cols.y.values()):
                col.add(row.cell[col.at])
                    
    #Data:stats function
    def stats(self, places, showCols, fun):
        showCols = showCols or self.cols.y
        fun = fun or "mid"
        t = {}
        for _, col in showCols.items():
            print(col)
            if fun == "mid":
                v = col.mid()
            else:
                v = col.div()
            v = rnd(v, places) if isinstance(v, int) else v
            t[col.name] = v

        return t


