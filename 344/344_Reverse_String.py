class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if s is None or len(s) < 2:
            return
        for i in xrange(len(s)/2):
            self.swap(s,i, -(i+1))
        return s

    def swap(self, s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

test = Solution()
print test.reverseString(["h","e","l","l","o"]) # ["o","l","l","e","h"]
print test.reverseString(["H","a","n","n","a","h"]) # ["h","a","n","n","a","H"]
print test.reverseString(["h","e"]) # ["e","h"]
print test.reverseString(["h","e", "l"]) # ["l","e","h"]