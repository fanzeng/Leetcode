class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.d = {}
        return self.minDistanceDP(word1, word2)

    def minDistanceDP(self, word1, word2):
        if word1 is None or len(word1) == 0:
            return len(word2)
        if word2 is None or len(word2) == 0:
            return len(word1)
        if self.d.get((word1, word2)) is not None:
            return self.d[(word1, word2)]

        if word1[0] == word2[0]:
            return self.minDistanceDP(word1[1:], word2[1:])
        res1 = 1 + self.minDistanceDP(word1[1:], word2)
        res2 = 1 + self.minDistanceDP(word1, word2[1:])
        res = min(res1, res2)
        self.d[(word1, word2)] = res
        return res

test = Solution()
print test.minDistance('sea', 'eat') # 2
print test.minDistance("leetcode", "etco") # 4