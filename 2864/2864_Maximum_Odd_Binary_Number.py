class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        counts = sum([1 for c in chars if c == '1'])
        # print counts
        if counts == 1:
            return "0"*(len(chars) - 1) + "1"
        return "1"*(counts - 1) + "0"*(len(chars) - counts) + "1"
