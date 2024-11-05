class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        sz = len(s)
        res = [0]*(sz + 1)
        i = sz - 2
        while i >= 0:
            curr = 0
            if (s[i] == '0' and s[i+1] == '1') or (s[i] == '1' and s[i+1] == '0'):
                curr = 1
            res[i] = curr + res[i+2]
            i -= 2
        return res[0]
