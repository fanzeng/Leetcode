class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.m = len(matrix)
        self.n = len(matrix[0])
        zero_row = set()
        zero_col = set()
        for i in xrange(self.m):
            for j in xrange(self.n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        for row in zero_row:
            for c in xrange(self.n):
                matrix[row][c] = 0
        for col in zero_col:
            for r in xrange(self.m):
                matrix[r][col] = 0

        return matrix

test = Solution()
print test.setZeroes([[1,1,1],[1,0,1],[1,1,1]]) # [[1,0,1],[0,0,0],[1,0,1]]
print test.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]