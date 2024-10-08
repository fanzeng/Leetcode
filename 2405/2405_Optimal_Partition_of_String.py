class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        d = {}
        count = 1
        i = 0
        while i < len(s):
            if d.get(s[i]) is None:
                d[s[i]] = True
                i += 1
            else:
                count += 1
                d = {}
        return count
