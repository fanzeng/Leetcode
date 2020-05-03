# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """

class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat

    def get(self, x, y):
       """
       :type x : int, y : int
       :rtype int
       """
       return self.mat[x][y]

    def dimensions(self):
       """
       :rtype list[]
       """
       return [len(self.mat), len(self.mat[0])]

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows = binaryMatrix.dimensions()[0]
        cols = binaryMatrix.dimensions()[1]
        min_c = cols
        for r in xrange(rows):
            min_c_candidate = self.leftMostColumnWithOneSingleRow(binaryMatrix, r, min_c, cols)
            if min_c_candidate != -1:
                min_c = min(min_c, min_c_candidate)
        if min_c < cols:
            return min_c
        else:
            return -1

    def leftMostColumnWithOneSingleRow(self, binaryMatrix, row, col, cols):
        l = 0
        r = min(col, cols-1)
        while l < r-1:
            m = (l + r) / 2
            if binaryMatrix.get(row, m) == 1:
                r = m
                m = (l + r) / 2
            else:
                l = m
                m = (l + r) / 2
        if binaryMatrix.get(row, l) == 1:
            return l
        if binaryMatrix.get(row, r) == 1:
            return r
        else:
            return -1

mat1 = [[0,0],[1,1]]
mat2 = [[0,0],[0,1]]
mat3 = [[0,0],[0,0]]
mat4 = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
test = Solution()
print test.leftMostColumnWithOne(BinaryMatrix(mat1))
print test.leftMostColumnWithOne(BinaryMatrix(mat2))
print test.leftMostColumnWithOne(BinaryMatrix(mat3))
print test.leftMostColumnWithOne(BinaryMatrix(mat4))