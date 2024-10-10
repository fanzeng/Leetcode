import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        q = []
        nums = sorted(nums)
        for n in nums:
            heapq.heappush(q, n)
        while q:
            a = heapq.heappop(q)
            if not q or a >= k:
                return res
            b = heapq.heappop(q)
            res += 1
            heappush(q, a*2 + b)
        return res
