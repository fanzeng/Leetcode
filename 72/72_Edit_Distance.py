class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.d = {}
        self.operations = ['insert', 'delete', 'replace']
        return self.minDistanceDP(word1, word2)

    def minDistanceDP(self, word1, word2):
        if word1 == word2 or ((word1 is None or len(word1) == 0) and (word2 is None or len(word2) == 0)):
            return 0
        if word1 is None or len(word1) == 0:
            return len(word2)
        if word2 is None or len(word2) == 0:
            return len(word1)
        res = self.d.get(word1 + '_' + word2)
        if res is not None:
            return res
        if word1[0] == word2[0]:
            res = self.minDistanceDP(word1[1:], word2[1:])
        else:
            resInsert = 1 + self.minDistanceDP(word1, word2[1:])
            resDelete = 1 + self.minDistanceDP(word1[1:], word2)
            resReplace = 1 + self.minDistanceDP(word1[1:], word2[1:])
            res = min([resInsert, resDelete, resReplace])
            # print res, word1, word2, self.operations[self.argmin([resInsert, resDelete, resReplace])]
        self.d[word1 + '_' + word2] = res
        return res

    def argmin(self, l):
        return min(range(len(l)), key=lambda x: l[x])

test = Solution()
print test.minDistance("horse", "ros") # 3
print test.minDistance("intention", "execution") # 5