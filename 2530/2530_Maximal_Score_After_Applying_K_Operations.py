import heapq

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        for n in nums:
            heapq.heappush(q, (-n, n))
        
        score = 0
        for i in range(k):
            s = heapq.heappop(q)
            score += s[1]
            new_s = int(ceil(float(s[1])/3))
            heapq.heappush(q, (-new_s, new_s))
        return score
