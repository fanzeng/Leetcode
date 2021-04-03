class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        self.d = [[[-1 for one in range(n+1)] for zero in range(m+1)] for s in xrange(len(strs)+1)]
        self.lCountZero = []
        self.lCountOne = []
        for s in strs:
            self.lCountZero.append(s.count('0'))
            self.lCountOne.append(s.count('1'))
        return self.findMaxFormDP(strs, m, n)

    def findMaxFormDP(self, strs, maxZero, maxOne):
        if strs is None or len(strs) == 0 or (maxZero == 0 and maxOne == 0):
            return 0
        if self.d[len(strs)][maxZero][maxOne] != -1:
            return self.d[len(strs)][maxZero][maxOne]
        countZero = self.lCountZero[len(self.lCountZero)-len(strs)]
        countOne = self.lCountOne[len(self.lCountOne)-len(strs)]
        resNotInclude = self.findMaxFormDP(strs[1:], maxZero, maxOne)
        if maxZero - countZero < 0 or maxOne - countOne < 0:
            self.d[len(strs)][maxZero][maxOne] = resNotInclude
            return resNotInclude
        res = max(
            self.findMaxFormDP(strs[1:], maxZero - countZero, maxOne - countOne) + 1,
            resNotInclude
        )
        self.d[len(strs)][maxZero][maxOne] = res
        return res

test = Solution()
print test.findMaxForm(["10","0001","111001","1","0"], 5, 3) # 4
print test.findMaxForm(["10","0001","111001","1","0"], 4, 3) # 3
print test.findMaxForm(["10","0","1"], 1, 1) # 2
print test.findMaxForm(["00","000"], 1, 10) # 0