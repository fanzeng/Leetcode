class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            m = n/2
            if m*2 == n:
                n = m
            else:
                return False
        return True