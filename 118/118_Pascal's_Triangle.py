class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[-1][j-1]+res[-1][j])
            row.append(1)
            res.append(row)
        return res
test = Solution()
for i in range(10):
    print 'test.generate(' + str(i) + ') =', test.generate(i)
