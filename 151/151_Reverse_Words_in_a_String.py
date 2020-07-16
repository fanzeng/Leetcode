class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split(' ')
        words.reverse()
        return ' '.join([w for w in words if len(w.strip()) > 0]).strip()

test = Solution()
print test.reverseWords("the sky is blue") # "blue is sky the"
print test.reverseWords("  hello world!  ") # "world! hello"
print test.reverseWords("a good   example") # "example good a"