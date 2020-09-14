class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        prod_since_reset_pos = None
        prod_since_reset_neg = None
        if nums[0] >= 0:
            prod_since_reset_pos = nums[0]
        elif nums[0] < 0:
            prod_since_reset_neg = nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            prod_since_reset_new_0 = None
            prod_since_reset_new_1 = None
            if prod_since_reset_pos is not None:
                prod_since_reset_new_0 = prod_since_reset_pos*nums[i]
            if prod_since_reset_neg is not None:
                prod_since_reset_new_1 = prod_since_reset_neg*nums[i]
            temp_max = max([val for val in [nums[i], prod_since_reset_new_0, prod_since_reset_new_1] if val is not None])
            temp_min = min([val for val in [nums[i], prod_since_reset_new_0, prod_since_reset_new_1] if val is not None])

            if temp_max >= 0:
                prod_since_reset_pos = temp_max
            else:
                prod_since_reset_pos = None
            if temp_min < 0:
                prod_since_reset_neg = temp_min
            else:
                prod_since_reset_neg = None
            # print nums[i], temp_max, temp_min, prod_since_reset_pos, prod_since_reset_neg
            max_prod = max([max_prod, prod_since_reset_pos])
        return max_prod

test = Solution()
print test.maxProduct([2,3,-2,4]) # 6
print test.maxProduct([-2,0,-1]) # 0
print test.maxProduct([-2,3,-4]) # 24
print test.maxProduct([-1,-2,-9,-6]) # 108
print test.maxProduct([2,-5,-2,-4,3]) # 24
print test.maxProduct([-1,-1,0]) # 1