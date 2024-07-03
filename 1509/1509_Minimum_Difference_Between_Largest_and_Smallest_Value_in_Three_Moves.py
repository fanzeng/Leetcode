class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) == min(nums):
            return nums
        sn = sorted(nums)
        # print sn
        nums = self.make_move(sn, 3)
        return nums[-1] - nums[0]

    def make_move(self, nums, remaining_moves):
        # print nums
        if remaining_moves == 0:
            return nums
        if len(nums) == 2:
            return [nums[0], nums[0]]
        remove_min = self.make_move(nums[1:], remaining_moves - 1)
        remove_max = self.make_move(nums[:-1], remaining_moves - 1)
        if remove_max[-1] - remove_max[0] > remove_min[-1] - remove_min[0]:
            return remove_min
        else:
            return remove_max
