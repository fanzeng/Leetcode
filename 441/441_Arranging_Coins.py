class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n = k(k+1)/2, n, k are integers. Solve k.
        if n <= 0:
            return 0
        if n == 1:
            return 1
        l = 1
        r = n
        m = (l+r)/2
        while l < r-1:
            if m*(m+1) == n*2:
                break
            elif m*(m+1) > n*2:
                r = m
            else:
                l = m
            m = (l+r)/2
        return m

test = Solution()
print test.arrangeCoins(1) # 1
print test.arrangeCoins(5) # 2
print test.arrangeCoins(8) # 3