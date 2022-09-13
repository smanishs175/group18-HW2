
from settings import the
from src.readCSV import *
from src.utils import push, rnd
from src.cols import Cols
from src.row import Row

class Data:
    
    #Data:new function
    def __init__(self, src, theObj=the()):
        self.rows = []
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
            # cells = xs.cell if xs else Row(xs)
            row = push(self.rows, Row(row))
            for _,todo in zip(self.cols.x, self.cols.y):
                for _, col in todo.items():
                    col.add(row.cell[col.at])


    #Data:stats function
    def stats(self, places, showCols, fun, t,v):
        showCols = showCols or self.cols.y
        fun = fun or "mid"
        t = {}
        for _, col in showCols.items():
            if fun == "mid":
                v = col.mid()
            else:
                v = col.div()
            v = rnd(v, places) if isinstance(v, int) else v
            t[col.name] = v

        return t


