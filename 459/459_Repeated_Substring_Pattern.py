class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for div in xrange(2, length+1):
            if length % div != 0:
                continue
            substr = s[:length/div]
            substr_repeated = substr*div
            if substr_repeated == s:
                return True
        return False


test = Solution()
print test.repeatedSubstringPattern("abab") # True
print test.repeatedSubstringPattern("aba") # False
print test.repeatedSubstringPattern("abcabcabcabc") # True
print test.repeatedSubstringPattern("bb") # True