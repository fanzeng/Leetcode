class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        self.ugly = set([1])
        count = 0
        while count < n:
            curr = min(self.ugly)
            self.ugly.remove(curr)
            self.ugly.update([curr*2, curr*3, curr*5])
            count += 1
        return curr
