class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        self.matrix = matrix
        self.k = k
        self.d = {(0,0,0,0): self.matrix[0][0]}
        for i0 in xrange(len(self.matrix)):
            for j0 in xrange(len(self.matrix[0])):
                for i1 in xrange(i0, len(self.matrix)):
                    for j1 in xrange(j0, len(self.matrix[0])):
                        sum = self.sumSubmatrixDP(i0, j0, i1, j1)
                        # print i0, j0, i1, j1, sum
                        if sum == self.k:
                            return sum
                        self.d[(i0, j0, i1, j1)] = sum
        # print self.d
        return max([v for v in self.d.values() if v < self.k])

    def sumSubmatrixDP(self, i0, j0, i1, j1):
        if self.d.get((i0, j0, i1, j1)) is not None:
            return self.d[(i0, j1, i1, j1)]
        if self.d.get((i0, j0, i1, j1-1)) is not None:
            sum_col = 0
            for row in xrange(i0, i1+1):
                sum_col += self.matrix[row][j1]
            return self.d[(i0, j0, i1, j1-1)] + sum_col

        if self.d.get((i0, j0, i1-1, j1)) is not None:
            sum_row = 0
            for col in xrange(j0, j1+1):
                sum_row += self.matrix[i1][col]
            return self.d[(i0, j0, i1-1, j1)] + sum_row
        if i0 == i1:
            if j0 == j1:
                return self.matrix[i0][j0]
            else:
                sum_row = 0
                for col in xrange(j0, j1+1):
                    sum_row += self.matrix[i0][col]
                return self.d[(i0, j0, i1, j1 - 1)] + sum_row

test = Solution()
print test.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2) # 2
print test.maxSumSubmatrix([[2,2,-1]], 3) # 3
print test.maxSumSubmatrix([[2,2,-1]], 0) # -1