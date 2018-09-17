class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = 0
		i = 0
		if len(nums) < 1:
			return 0
		while i < len(nums)-1:
			i += 1
			if nums[i] != nums[count]:
				count += 1
				nums[count] = nums[i]
		# print nums
		return count+1


test = Solution()
print test.removeDuplicates([1, 2, 2])
print test.removeDuplicates([1, 1, 2])
print test.removeDuplicates([1, 2, 2, 3])
print test.removeDuplicates([1, 1, 2, 3])
print test.removeDuplicates([1])
print test.removeDuplicates([1, 1, 1, 1])
print test.removeDuplicates([1, 1, 1, 1, 2])

print test.removeDuplicates([])
print test.removeDuplicates([1, 1, 2])


