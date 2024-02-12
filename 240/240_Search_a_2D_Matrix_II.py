class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.find_in_submatrix(matrix, target)

    def find_in_submatrix(self, matrix, target):
        # print matrix
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        if rows == 1:
            return target in matrix[0]
        if cols == 1:
            return target in [row[0] for row in matrix]
        if rows == 2 and cols == 2:
            return matrix[0][0] == target or matrix[0][1] == target or matrix[1][0] == target or matrix[1][1] == target
        v = matrix[rows/2][cols/2]
        if v == target:
            return True
        b = self.find_in_submatrix([row[cols/2+1:] for row in matrix[:rows/2+1]], target)
        c = self.find_in_submatrix([row[:cols/2+1] for row in matrix[rows/2+1:]], target)
        if v > target:
            a = self.find_in_submatrix([row[:cols/2+1] for row in matrix[:rows/2+1]], target)
            return a or b or c
        else:
            a = self.find_in_submatrix([row[cols/2+1:] for row in matrix[rows/2+1:]], target)
            return a or b or c
