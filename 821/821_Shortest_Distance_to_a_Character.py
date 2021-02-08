class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        indices = []
        for i, char in enumerate(s):
            if c == char:
                indices.append(i)
        # print indices
        res = []
        for i in xrange(len(s)):
            res.append(min([abs(i-index) for index in indices]))
        return res

test = Solution()
print test.shortestToChar("loveleetcode", "e") # [3,2,1,0,1,0,0,1,2,2,1,0]
print test.shortestToChar("aaab", "b") # [3,2,1,0]