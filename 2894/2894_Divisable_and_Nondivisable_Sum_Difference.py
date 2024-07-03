class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nums1 = [n for n in range(1, n+1) if n % m != 0]
        nums2 = [n for n in range(1, n+1) if n % m == 0]
        return sum(nums1) - sum(nums2)
