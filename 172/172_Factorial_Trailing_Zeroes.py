class Solution(object):
    def trailingZeroes(self, n):
        if n < 5:
            return 0
        if n < 10:
            return 1
        b = 5
        power = 1
        while b <= n:
            b *= 5
            power += 1
        res = 0
        for p in xrange(1, power):
            res += n/(5**p)
        return res

# TLE, after passing 500/502 cases
    # def trailingZeroes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 0:
    #         return 0
    #     res = 0
    #     for i in xrange(1, n+1):
    #         while i / 5 * 5 == i:
    #             res += 1
    #             i /= 5
    #     return res

test = Solution()
print test.trailingZeroes(3)
print test.trailingZeroes(5)
print test.trailingZeroes(6)
print test.trailingZeroes(15)
print test.trailingZeroes(20)
print test.trailingZeroes(25)
print test.trailingZeroes(30)
print test.trailingZeroes(50)
print test.trailingZeroes(120)
print test.trailingZeroes(125)