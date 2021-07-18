class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        if row*col == 0 or r*c == 0 or row*col != r*c:
            return mat
        res = []
        self.mat = mat
        self.i = 0
        self.j = 0
        self.col = col
        for k in xrange(r):
            a = []
            for l in xrange(c):
                a.append(self.nextNum())
            res.append(a)
        return res

    def nextNum(self):
        if self.j == self.col:
            self.i += 1
            self.j = 0
        num = self.mat[self.i][self.j]
        self.j += 1
        return num

test = Solution()
print test.matrixReshape([[1,2],[3,4]], 1, 4) # [[1,2,3,4]]
print test.matrixReshape([[1,2],[3,4]], 2, 4) # [[1,2],[3,4]]
print test.matrixReshape([[1,2,3],[4,5,6]], 1, 6) # [[1,2,3,4,5,6]]
print test.matrixReshape([[1,2,3],[4,5,6]], 3, 2) # [[1,2],[3,4],[5,6]]
print test.matrixReshape([[1]], 1, 1) # [[1]]