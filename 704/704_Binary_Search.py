class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        while l + 1 < r:
            m = (l+r) / 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m
            else:
                r = m
        if nums[l] == target:
            return l
        return -1

test = Solution()
print test.search([-1,0,3,5,9,12], 9) # 4
print test.search([-1,0,3,5,9,12], target = 2) # -1