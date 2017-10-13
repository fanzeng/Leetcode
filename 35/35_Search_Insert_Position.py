class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		for i in range(len(nums)):
			if nums[i] >= target:
				return i
		return len(nums)


test = Solution()
print test.searchInsert([1,3,5,6], 5)
print test.searchInsert([1,3,5,6], 2)
print test.searchInsert([1,3,5,6], 7)
print test.searchInsert([1,3,5,6], 0)
