class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) < 2:
            return matrix
        self.matrix = matrix
        self.n = len(matrix)
        if self.n % 2 == 0:
            for i in xrange(self.n/2):
                for j in xrange(self.n/2):
                    self.rotateOne(i, j)
        else:
            for i in xrange(self.n/2):
                for j in xrange(self.n/2+1):
                    self.rotateOne(i, j)
        return matrix

    def rotateOne(self, i, j):
        n = self.n
        loop = [self.matrix[i][j], self.matrix[j][n-1-i], self.matrix[n-1-i][n-1-j], self.matrix[n-1-j][i]]
        loop_rotated = [loop[-1]]+loop[:-1][:]
        # print loop_rotated
        self.matrix[i][j] = loop_rotated[0]
        self.matrix[j][n-1-i] = loop_rotated[1]
        self.matrix[n-1-i][n-1-j] = loop_rotated[2]
        self.matrix[n-1-j][i] = loop_rotated[3]

test = Solution()
print test.rotate([[1,2,3],[4,5,6],[7,8,9]]) # [[7,4,1],[8,5,2],[9,6,3]])
print test.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
print test.rotate([[1]]) # [[1]]
print test.rotate([[1,2],[3,4]]) # [[3,1],[4,2]])