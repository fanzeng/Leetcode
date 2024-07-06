class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        # every n - 1 steps it reaches one of the end points
        return 1 + time % (n - 1) if (time / (n - 1)) % 2 == 0 else n - time % (n - 1)
