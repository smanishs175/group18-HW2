import random

from settings import the
from src.utils import percentile


class Num:

    def __init__(self, c, s, theObj=the()):
        self.n = 0
        self.at = c or 0
        self.name = s or ""
        self.isSorted = False
        self.theObj = theObj
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

    def add(self, v):
        pos = -1
        if v != "?":
            self.n += 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
            if self.n <= self.theObj.nums:
                self._has.append(v)
            elif random.random() < self.theObj.nums / self.n:
                pos = random.randint(0, len(self._has) - 1)
            if pos != -1:
                self.isSorted = False
                self._has[pos] = int(v)

    def mid(self):
        a = self.nums()
        n = len(a)
        if n == 0:
            return 0
        elif n in [1,2]:
            return a[0]

        if n % 2 == 0:
            return (a[n//2] + a[n//2 - 1])/2
        else:
            return a[n//2 - 1]

    def div(self):
        a = self.nums()
        return (percentile(a, 90) - percentile(a, 10))/2.56
