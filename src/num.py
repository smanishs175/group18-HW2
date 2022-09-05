class Num:

    def __init__(self):
        self.isSorted = False
        self._has = []
        self.lo = float('inf')
        self.hi = -float('inf')
        self.w = []
    
    def nums(self):
        if self.isSorted:
            return self._has

        self._has.sort()
        self.isSorted = True
        return self._has
