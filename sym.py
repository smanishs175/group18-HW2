class Sym:

    def __init__(self,dict):
        self.dict=dict

    def mid(self,col,most,mode):
        most=-1
        for k,v in self.dict:
            if v>most:
                mode,most=k,v
        return mode


