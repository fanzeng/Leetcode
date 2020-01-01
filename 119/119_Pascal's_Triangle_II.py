class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        res = [1, 1]
        for i in range(1, rowIndex+1):
            new_res = [1]
            for j in range(1, i):
                new_res.append(res[j] + res[j-1])
            res = new_res + [1]
        return res

test = Solution()
for i in range(10):
    print 'test.getRow('+ str(i) + ') =', test.getRow(i)
