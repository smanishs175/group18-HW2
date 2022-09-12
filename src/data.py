
from settings import the
from src.readCSV import *

class Data:
    
    #Data:new function
    def __init__(self, src, theObj=the()):
        self.rows = {}
        self.cols = None
        if type(src) == "string":
            Csv(src=src, sep = theObj.separator, fun=lambda x: self.add(x))
        else:
            for _, row in src.items():
                self.add(row)
    #Data:add function
    def add(self, row):
        pass



