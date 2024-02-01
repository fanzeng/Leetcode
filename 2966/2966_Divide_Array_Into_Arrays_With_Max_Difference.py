class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums)/3):
            arr = nums[i*3:i*3+3]
            if self.satisfy(arr, k):
                res.append(arr)
            else:
                return []
        return res
    
    def satisfy(self, arr, k):
        return (arr[0] - arr[1] <= k) and (arr[1] - arr[0] <= k) and (arr[2] - arr[0] <= k)
