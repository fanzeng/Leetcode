class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findDuplicateRecursive(nums)

    def findDuplicateRecursive(self, nums):
        if len(nums) < 2:
            return -1
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return nums[0]
            else:
                return -1
        nums_0 = nums[:len(nums)/2+1]
        nums_1 = nums[len(nums)/2+1:]
        res_two_array = self.findDuplicateTwoArray(nums_0, nums_1)
        if res_two_array > 0:
            return res_two_array
        return max(self.findDuplicateRecursive(nums_0), self.findDuplicateRecursive(nums_1))

    def findDuplicateTwoArray(self, nums_0, nums_1):
        for i in xrange(len(nums_0)):
            for j in xrange(len(nums_1)):
                if nums_0[i] == nums_1[j]:
                    return nums_0[i]
        return -1

test = Solution()
print test.findDuplicate([1,3,4,2,2]) # 2
print test.findDuplicate([3,1,3,4,2]) # 3
print test.findDuplicate([5,1,5,5,5]) # 5

