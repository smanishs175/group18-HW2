import math

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


    def mid(self,col=0,most = -1,mode=0):

        for k, v in self._has.items():
            if v > most:
                mode, most = k, v
        return mode
    

    def add(self,v):
        if v != '?':
            self.n = self.n + 1
            value = 0

            if v in self._has:
                value = self._has[v] + 1
            else:
                value = 1
            self._has[v] = value    
            
       
    def fun(p):
        return p * math.log(p, 2) 
    
    
    def div(self, e=0, fun = fun):
        for _,n in self._has.items():
            if n > 0:
                e = e - fun(n/self.n)
        return e










