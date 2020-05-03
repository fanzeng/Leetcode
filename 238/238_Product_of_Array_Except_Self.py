class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        l = 0
        r = -1
        right_product = nums[r]
        d = {}
        d[r] = right_product
        while True:
            r -= 1
            right_product *= nums[r]
            d[r] = right_product
            if r == -len(nums):
                break
        li = [d[-(len(nums)-1)]]
        l_product = nums[0]
        for i in xrange(1, len(nums)-1):
            p = l_product*d[-(len(nums)-i-1)]
            li.append(p)
            l_product *= nums[i]
        li.append(l_product)
        return li

test = Solution()
print test.productExceptSelf([1,2,3,4]) # [24,12,8,6]
print test.productExceptSelf([2,3,5,0]) # [0,0,0,30]