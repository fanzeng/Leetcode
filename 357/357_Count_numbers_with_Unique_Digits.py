class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        choice = 9
        prod = 9
        digit = 1
        while digit < n:
            prod *= choice
            choice -= 1
            digit += 1
        return self.countNumbersWithUniqueDigits(n - 1) + prod
