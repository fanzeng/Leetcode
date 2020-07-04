class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N == 0:
            return cells
        self.cells = cells
        self.d = {}
        i = 0
        while i < N:
            i += 1
            if not self.nextDay(i):
                break
            for (k, v) in self.d.items():
                if self.isListSame(v, self.cells):
                    period = i - k
                    # print 'period =', period
                    if N % period == 0:
                        self.cells = self.d[period]
                    else:
                        self.cells = self.d[N%period]
                    N = 0
                    break
            if N != 0:
                self.d[i] = self.cells

        return self.cells

    def nextDay(self, day):
        cells = []
        cells.append(0)
        for i in xrange(1, len(self.cells)-1):
            if self.cells[i-1] == self.cells[i+1]:
                cells.append(1)
            else:
                cells.append(0)
        cells.append(0)
        changed = not self.isListSame(self.cells, cells)
        self.cells = cells
        # print day, cells
        return changed

    def isListSame(self, a, b):
        isSame = True
        for (aa, bb) in zip(a, b):
            if aa != bb:
                isSame = False
                break
        return isSame

test = Solution()
print test.prisonAfterNDays([0,1,0,1,1,0,0,1], 7) # [0,0,1,1,0,0,0,0]
print test.prisonAfterNDays([1,0,0,1,0,0,1,0], 50) # [0,1,0,0,1,0,0,0]
print test.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000) # [0,0,1,1,1,1,1,0]
print test.prisonAfterNDays([0,0,0,1,1,0,1,0], 574) # [0,0,0,1,1,0,1,0]
print test.prisonAfterNDays([1,0,0,1,0,0,0,1], 826) # [0,1,1,0,1,1,1,0]