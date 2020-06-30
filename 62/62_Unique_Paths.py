class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.m = m # m is column number
        self.n = n # n is row number
        self.d = {}
        for col in xrange(self.m):
            self.d[self.getHash(self.n-1, col)] = 1
        for row in xrange(self.n):
            self.d[self.getHash(row, self.m-1)] = 1
        self.uniquePathsDP()
        return self.d[self.getHash(0, 0)]

    def uniquePathsDP(self):
        for i in xrange(self.n-2, -1, -1):
            for j in xrange(self.m-2, -1, -1):
                self.d[self.getHash(i, j)] = self.d[self.getHash(i+1, j)] + self.d[self.getHash(i, j+1)]

    def getHash(self, r, c):
        return r*self.m + c


test = Solution()
print test.uniquePaths(3, 2) # 3
print test.uniquePaths(7, 3) # 28
print test.uniquePaths(1, 1) # 1
print test.uniquePaths(2, 2) # 2
print test.uniquePaths(3, 7) # 28
