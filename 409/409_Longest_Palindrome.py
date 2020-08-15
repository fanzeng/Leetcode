class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            if d.get(c) is None:
                d[c] = 1
            else:
                d[c] += 1
        # print d
        length = 0
        has_odd = False
        for v in d.values():
            if v % 2 == 0:
                length += v
            else:
                has_odd = True
                length += v-1
        return length + int(has_odd)

test = Solution()
print test.longestPalindrome("abccccdd") # 7