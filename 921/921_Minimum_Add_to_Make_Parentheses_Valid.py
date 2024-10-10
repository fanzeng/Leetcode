class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack = []
        count = 0
        res = 0
        for c in s:
            if c == '(':
                # stack.append(c)
                count += 1
            else:
                if count > 0:
                    # stack = stack[:-1]
                    count -= 1
                else:
                    res += 1
        return res + count
