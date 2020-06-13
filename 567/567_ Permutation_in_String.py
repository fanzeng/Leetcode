class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s2) < len(s1) or s2 is None:
            return False
        if s1 is None or len(s1) == 0:
            return True
        h_s1 = self.getHash(s1)
        s2_begin = s2[:len(s1)]
        h_0 = self.getHash(s2_begin)
        if h_0 == h_s1:
            return True
        h_prev = h_0
        for i in xrange(1, len(s2)-len(s1)+1):
            h_i = self.modHash(h_prev, s2[i-1], s2[i+len(s1)-1])
            if h_i == h_s1:
                return True
            h_prev = h_i
        return False

    def getHash(self, s):
        h = 0
        for c in s:
            h += 2**(ord(c)-ord('a')+1)
        return h

    def modHash(self, h, drop, add):
        return h - 2**(ord(drop)-ord('a')+1) + 2**(ord(add)-ord('a')+1)

test = Solution()
print test.checkInclusion("ab", "eidbaooo") # True
print test.checkInclusion("ab", "eidboaoo") # False

