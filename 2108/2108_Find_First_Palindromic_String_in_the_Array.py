class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if self.isPalindromic(word):
                return word
        return ""

    def isPalindromic(self, word):
        chars = list(word)
        if len(chars) == 0:
            return False
        l = 0
        r = len(chars) - 1
        while l < r:
            if chars[l] != chars[r]:
                return False
            l += 1
            r -= 1
        return True
