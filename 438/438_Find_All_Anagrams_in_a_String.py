class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p) or s is None or p is None:
            return []
        res = []
        h_p = self.getHash(p)
        s_begin = s[:len(p)]
        h_0 = self.getHash(s_begin)
        if h_0 == h_p:
            res.append(0)
        h_prev = h_0
        for i in xrange(1, len(s)-len(p)+1):
            h_i = self.modHash(h_prev, s[i-1], s[i+len(p)-1])
            if h_i == h_p:
                res.append(i)
            h_prev = h_i
        return res

    def getHash(self, s):
        h = 0
        for c in s:
            h += 2**(ord(c)-ord('a')+1)
        return h

    def modHash(self, h, drop, add):
        return h - 2**(ord(drop)-ord('a')+1) + 2**(ord(add)-ord('a')+1)

test = Solution()
print test.findAnagrams("cbaebabacd", "abc") # [0, 6]
print test.findAnagrams("abab", "ab") # [0, 1, 2]
print test.findAnagrams("ab", "abcd") # []
print test.findAnagrams("abcdefghabcdefgh", "abcdefgh") # [0, 1, 2, 3, 4, 5, 6, 7, 8]
