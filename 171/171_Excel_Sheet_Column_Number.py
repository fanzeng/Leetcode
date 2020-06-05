class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = 26
        num = ord(s[-1])-ord('A')
        for i in xrange(len(s)-2, -1, -1):
            num += b*(ord(s[i])-ord('A') + 1)
            b *= 26
        return num + 1

test = Solution()
print test.titleToNumber("A") # 1
print test.titleToNumber("AB") # 28
print test.titleToNumber("ZY") # 701
print test.titleToNumber("Z") # 26