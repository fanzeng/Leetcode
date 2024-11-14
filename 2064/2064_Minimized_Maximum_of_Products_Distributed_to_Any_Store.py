class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        q = quantities
        l = 1
        r = max(q)
        while r > l:
            m = l + (r - l) / 2
            if self.canDist(n, q, m):
                r = m
            else:
                l = m + 1
        return l

    # Check if k is a possible x
    def canDist(self, n, q, k):
        count = 0
        for amount in q:
            quot = amount / k
            if amount % k == 0:
                count += quot
            else:
                count += quot + 1
            if count > n:
                return False
        return True
