import random

from settings import the


class Num:

    def __init__(self, c, s):
        self.n = 0
        self.at = c or 0
        self.name = s or ""
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

    def add(self, v):
        pos = -1
        theObj = the()

        if v != "?":
            self.n += 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
            if len(self._has) < theObj.nums:
                pos = 1 + len(self._has)
            elif random.random() < theObj.nums / self.n:
                pos = random.randint(0, len(self._has))
            if pos != -1:
                self.isSorted = False
                self._has[pos] = int(v)

    def mid(self):
        a = self.nums()
        percentile90 = (a[-1] - a[0]) * 0.9
        percentile10 = (a[-1] - a[0]) * 0.1
        return (percentile90 - percentile10) / 2.58

    def div(self):
        a = self.nums()
        percentile50 = (a[-1] - a[0]) * 0.5
        return percentile50
