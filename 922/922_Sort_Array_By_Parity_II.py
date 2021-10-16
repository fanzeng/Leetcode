class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_odd = 0
        count_even = 0
        res = [None]*len(nums)
        for num in nums:
            if num % 2 == 0:
                res[2*count_even] = num
                count_even += 1
            else:
                res[2*count_odd+1] = num
                count_odd += 1
        return res