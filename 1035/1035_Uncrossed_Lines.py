class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if A is None or len(A) == 0 or B is None or len(B) == 0:
            return 0
        dB = self.toDict(B)
        res = [[0]*len(B)]*len(A)
        if dB.get(A[-1]) is not None:
            res[len(A)-1][:max(dB.get(A[-1]))+1] = [1]*(max(dB.get(A[-1]))+1)
        for i in xrange(len(A)-2, -1, -1):
            dBRes = dB.get(A[i])
            for j in xrange(len(B)):
                if dBRes is not None and max(dBRes) >= j:
                    mindBRes = min([x for x in dBRes if x >= j])
                    if mindBRes == len(B)-1:
                        res[i][j] = max(res[i+1][j], 1)
                    else:
                        res[i][j] = max(res[i+1][j], 1 + res[i+1][mindBRes+1])
                else:
                    res[i][j] = res[i + 1][j]
        return res[0][0]

    def toDict(self, A):
        d = {}
        for i, n in enumerate(A):
            if d.get(n) is not None:
                d.get(n).append(i)
            else:
                d[n] = [i]
        return d

test = Solution()
print test.maxUncrossedLines([1,4,2], [1,2,4]) # 2
print test.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]) # 3
print test.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]) # 2