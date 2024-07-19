class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for row in matrix:
            min_r = 10**5
            argmin = -1
            for i, n in enumerate(row):
                if n < min_r:
                    min_r = n
                    argmin = i
            if self.checkLucky(matrix, min_r, argmin):
                res.append(min_r)
        return res
    
    def checkLucky(self, matrix, num, col):
        for row in matrix:
            if row[col] > num:
                return False
        return True
