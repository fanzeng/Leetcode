class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        if n < 2:
            return n == 1
        while n > 1:
            if n/3*3 != n:
                return False
            n /= 3
        return True