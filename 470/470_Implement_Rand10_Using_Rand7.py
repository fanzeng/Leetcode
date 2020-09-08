# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        r2 = self.rand2()
        r5 = self.rand5()
        return 5*(r2-1) + r5

    def rand2(self):
        r = 0
        while r not in [1, 2]:
            r = rand7()
        return r

    def rand5(self):
        r = 0
        while r not in xrange(1, 6):
            r = rand7()
        return r

# rand7 is already defined, included here just for testing
def rand7():
    from random import randint
    return randint(1, 7)

test = Solution()
print test.rand2()
print test.rand5()
print test.rand10()