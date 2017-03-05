class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        d = {}
        length = 0
        strStart = 0
        for index in range(0, len(s)):
            if s[index] not in d:
                length += 1
                d[s[index]] = index
            else:
                if length > res:
                    res = length
                strStart = max((d[s[index]] + 1), strStart)
                length = index - strStart + 1
                d[s[index]] = index
                # d = {id: val for id, val in d.iteritems() if d[id] >= strStart}  # delete key in d before start of str
        if length > res:
            res = length
        return res

def main():
    test = Solution()
    s1 = 'abcabcbb'
    s2 = 'bbbbb'
    s3 = 'pwwkew'
    s4 = 'abcabcdabcd'
    s5 = 'abba'
    print test.lengthOfLongestSubstring(s1)
    print test.lengthOfLongestSubstring(s2)
    print test.lengthOfLongestSubstring(s3)
    print test.lengthOfLongestSubstring(s4)
    print test.lengthOfLongestSubstring(s5)

main()
