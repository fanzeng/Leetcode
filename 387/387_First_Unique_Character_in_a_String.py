class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        l_unique = []
        l_duplicate = []
        for c in s:
            if c in l_unique:
                l_unique.remove(c)
                l_duplicate.append(c)
            elif c not in l_duplicate:
                l_unique.append(c)
        if len(l_unique) > 0:
            return s.find(l_unique[0])
        else:
            return -1

test = Solution()
print test.firstUniqChar("eett") # -1
print test.firstUniqChar("leetcode") # 0
print test.firstUniqChar("loveleetcode") # 2.

# Note: You may assume the string contain only lowercase letters.