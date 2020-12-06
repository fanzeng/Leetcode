class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.sum = sum(nums)
        self.d = {}
        if self.sum % 2 != 0:
            return False
        self.target = self.sum / 2
        return self.canSumToTarget(nums, self.target)

    def canSumToTarget(self, nums, target):
        # print nums, target
        if len(nums) == 0:
            return target == 0
        if len(nums) == 1:
            return target == nums[0]
        h = self.getHash(nums, target)
        if self.d.get(h) is not None:
            return self.d[h]
        res = self.canSumToTarget(nums[1:], target - nums[0]) or self.canSumToTarget(nums[1:], target)
        self.d[h] = res
        return res

    def getHash(self, nums, target):
        return str(len(nums)) + ',' + str(target)

test = Solution()
print test.canPartition([1,5,11,5]) # True
print test.canPartition([1,2,3,5]) # False