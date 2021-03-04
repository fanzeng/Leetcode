class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = len(mat)
        if row == 0 or len(mat[0]) == 0:
            return 0
        sum = 0
        for i in xrange(row):
            sum += mat[i][i]
            sum += mat[row-1-i][i]
        if row % 2 == 1:
            sum -= mat[row/2][row/2]
        return sum

test = Solution()
print test.diagonalSum(
    [[1,2,3],
    [4,5,6],
    [7,8,9]]
) # 25
print test.diagonalSum(
    [[1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]]
) # 8
print test.diagonalSum([[5]]) # 5
print test.diagonalSum([[]]) # 0