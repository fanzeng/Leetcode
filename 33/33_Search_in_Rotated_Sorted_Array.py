# The following is a recursive solution that does not use the sorted property at all, but passes.
# class Solution(object):
# 	def search(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: int
# 		"""
#
# 		list_length = len(nums)
# 		if list_length == 0:
# 			return -1
# 		if list_length == 1:
# 			if nums[0] == target:
# 				return 0
# 			else:
# 				return -1
# 		mid = list_length / 2
# 		if target == nums[mid]:
# 			return mid
# 		else:
# 			left = self.search(nums[:mid], target)
# 			right = self.search(nums[mid:], target)
# 			if left != -1:
# 				return left
# 			elif right != -1:
# 				return mid + right
# 			else:
# 				return -1

class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if len(nums) == 0:
			return -1
		l = 0
		r = len(nums)-1
		while (l < r):
			mid = (l + r) / 2
			if nums[mid] == target:
				return mid
			if nums[mid] < nums[l]:
				if target < nums[mid]:
					r = mid - 1
				else:
					if target <= nums[r]:
						l = mid + 1
					else:
						r = mid - 1
			elif nums[mid] >= nums[r]:
				if target < nums[mid]:
					if target < nums[l]:
						l = mid + 1
					else:
						r = mid - 1
				else:
					l = mid + 1
			else:
				if target > nums[mid]:
					l = mid + 1
				elif target < nums[mid]:
					r = mid - 1
		if nums[r] == target:
			return r
		else:
			return -1

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [6,7,1,2,3,4,5]
# target = 6

# nums = [4,5,6,7,0,1,2]
# target = 3


# nums = [10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 4

# nums = []
# target = 2

test = Solution()
print test.search(nums, target)