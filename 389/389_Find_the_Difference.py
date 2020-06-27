class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c in t:
            if c not in s:
                return c
            else:
                s = s.replace(c, '', 1)

test = Solution()
print test.findTheDifference('a', 'aa')