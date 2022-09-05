class Sym:

    def __init__(self, c, s):
        self.n = 0
        self.at = 0
        self.name = ""
        self._has = {}
        if c:
            self.at = c
        if s:
            self.name = s
        return (self.n, self.at, self.name, self._has)


    def mid(self,col,most = -1,mode=0):

        for k, v in self._has.items():
            if v > most:
                mode, most = k, v
        return mode












