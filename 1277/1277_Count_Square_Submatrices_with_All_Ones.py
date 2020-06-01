class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        h = len(matrix)
        w = len(matrix[0])
        self.res = []
        for i in xrange(h):
            self.res.append([])
        res = 0
        for i in xrange(h):
            for j in xrange(w):
                size_max_square = self.findMaxSquare(matrix, i, j)
                # print i, j, size_max_square
                self.res[i].append(size_max_square)
                res += size_max_square
        return res

    def testNextSquare(self, matrix, i, j, size):
        if matrix[i+size-1][j+size-1] == 0:
            return False
        for delta in xrange(size):
            if matrix[i+delta][j+size-1] == 0 or matrix[i+size-1][j+delta] == 0:
                return False
        return True

    def maxPossibleSquare(self, matrix, i, j):
        h = len(matrix)
        w = len(matrix[0])
        return min(h-i, w-j)

    def findMaxSquare(self, matrix, i ,j):
        if matrix[i][j] == 0:
            return 0
        if i > 0 and j > 0:
            res_topleft = self.res[i-1][j-1]
            size_max_square = max(1, res_topleft-1)
        else:
            size_max_square = 1

        for size in xrange(size_max_square+1, self.maxPossibleSquare(matrix, i, j)+1):
            if not self.testNextSquare(matrix, i ,j, size):
                break
            size_max_square = size

        return size_max_square


test = Solution()
print test.countSquares(
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
) # 15

print test.countSquares(
    [
      [1,0,1],
      [1,1,0],
      [1,1,0]
    ]
) # 7