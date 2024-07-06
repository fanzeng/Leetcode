class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        # every n - 1 steps it reaches one of the end points
        direction = time / (n - 1)
        if direction % 2 == 0: # left to right
            return 1 + time % (n - 1)
        else:
            return n - time % (n - 1
