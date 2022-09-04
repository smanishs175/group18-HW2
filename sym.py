import math

class Sym:

    def __init__(self,c,s):
        self.n = 0
        self.at = 0
        self.name = ""
        self._has = {}
        if c:
            self.at = c
        if s:
            self.name = s
        return (self.n, self.at, self.name, self._has)
        
    def add(self,v):
        if v != '?':
            self.n = self.n + 1
            value = 0
            if self._has[v]:
                value = self._has[v] + 1
            self._has[v] = value    

    def mid(self,col,most,mode):
        most=-1
        for k,v in self._has.items():
            if v>most:
                mode,most=k,v
        return mode

    def fun(p):
        return p * math.log(p, 2) 
    
    
    def div(self, e=0, fun = fun):
        for _,n in self._has.items():
            if n > 0:
                e = e - fun(n/self.n)
        return e

    

     
        

     
      
             

