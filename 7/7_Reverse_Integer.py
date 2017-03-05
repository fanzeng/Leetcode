import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            y = -x # y is the absolute value of x
            z = self.get_z(y) # z is the absolute value of return value
            return - z
        else:
            return self.get_z(x)
    def get_z(self, y):
        z = 0
        while(y >= 1):
            z *= 10
            z +=y % 10
            y /=10
        if z >  2**31-1: #  sys.maxint:
            return 0  # do this to get pass Leetcode test cases
        else:
            return z


def main():
    test = Solution()
    print test.reverse(123)
    print test.reverse(1223)
    print test.reverse(-123)
    print test.reverse(1534236469)
    print test.reverse(-2147483412)
main()