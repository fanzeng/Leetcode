class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num < 4:
            return num == 1
        while num > 1:
            if num/4*4 != num:
                return False
            num /= 4
        return True