class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        i = 1
        while 10**i < x:
            i += 1
        i = max(0, (i-1)/2)
        l = 10**i
        r = 10**(i+1)+1
        while l < r:
            m = (l + r) / 2
            if m*m > x:
                r = m
            elif (m+1)*(m+1) > x:
                return m
            else:
                l = m

test = Solution()
print test.mySqrt(4)
print test.mySqrt(8)
print test.mySqrt(64)
print test.mySqrt(66)
print test.mySqrt(10000)
print test.mySqrt(1000000)
print test.mySqrt(100000000)
print test.mySqrt(123456789)
print test.mySqrt(183692038)


# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.