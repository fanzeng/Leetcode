class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        count = 0
        for f in xrange(1, n+1):
            if n % f == 0:
                count += 1
                if count == k:
                    return f
        return -1

test = Solution()
print test.kthFactor(12, 3) # 3
print test.kthFactor(7, 2) # 7
print test.kthFactor(4, 4) # -1
print test.kthFactor(1, 1) # 1
print test.kthFactor(1000, 3) # 4