class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(s) == len(t) and self.getHash(s, len(s)) == self.getHash(t, len(t))

    def getHash(self, s, l):
        h = 0
        for c in s:
            h += (l+1)**(ord(c) - ord('a'))
        return h

test = Solution()
print test.isAnagram("anagram", "nagaram") # True
print test.isAnagram("rat", "car") # False
print test.isAnagram("ac", "bb") # False
print test.isAnagram("dcccc", "bbbbe") # False