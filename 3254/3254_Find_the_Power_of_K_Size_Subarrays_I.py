class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1 or k == 1:
            return nums
        res = [-1]*(len(nums)-k+1)
        start = 0
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1] + 1:
                start = i
            if i >= k-1:
                if start <= i-k+1:
                    res[i-k+1] = nums[i]
            i += 1
        return res
