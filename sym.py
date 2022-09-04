import math

class Sym:

    def __init__(self,_has):
        self._has = _has
        
    def add(self,v):
        if v != '?':
            self.n = self.n + 1
            value = 0
            if self._has[v]:
                value = self._has[v] + 1
            self._has[v] = value    

    def mid(self,col,most,mode):
        most=-1
        for k,v in self._has:
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

    
    def new(self,c,s):
        self.n = 0
        at = 0
        name = ""
        self._has = {}
        if c:
            at = c
        if s:
            name = s
        return (self.n , at, name, self._has)
     
        

     
      
             

