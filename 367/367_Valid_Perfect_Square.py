class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        guess = 1
        while guess*guess < num:
            guess += 1
        if guess*guess == num:
            return True
        else:
            return False

test = Solution()
print test.isPerfectSquare(14)
print test.isPerfectSquare(16)
print test.isPerfectSquare(1600)
print test.isPerfectSquare(1500)