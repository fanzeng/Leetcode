class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.getHash(s) == self.getHash(t)

    def getHash(self, s):
        h = ''
        d = {}
        count = 0
        for c in s:
            if d.get(c) is None:
                d[c] = count
                count += 1
                h += str(count)
            else:
                h += str(d.get(c))
        return h


test = Solution()
print test.isIsomorphic("egg", "add") # True
print test.isIsomorphic("foo", "bar") # False
print test.isIsomorphic("paper", "title") # True
print test.isIsomorphic("abbbcccdddd", "sttteeeffff") # True