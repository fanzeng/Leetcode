class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) == 0:
            return len(s) == 0
        i = 0
        j = 0
        while i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1
            if j == len(t):
                return i == len(s)
        return True

test = Solution()
print test.isSubsequence("abc", "ahbgdc") # True
print test.isSubsequence("axc", "ahbgdc") # False