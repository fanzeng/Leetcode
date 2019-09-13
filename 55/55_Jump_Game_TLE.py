class Solution(object):
	def can_jump_dp(self, nums, start_pos):
		# print self.nums, start_pos
		if len(nums) == 1 or nums[0] >= len(nums)-1:
			return True
		elif nums[0] == 0:
			return False
		else:
			for i in range(nums[0], 0, -1):
				if self.can_jump_dp(self.nums[start_pos+i:], start_pos+i):
					return True
			self.nums[start_pos] = 0
			return False

	def canJump(self, nums):
		if min(nums) > 0:
			return True
		self.nums = nums
		return self.can_jump_dp(nums, 0)

test = Solution()
print test.canJump([2,3,1,1,4]) # expect True
print test.canJump([3,2,1,0,4]) # expect False
print test.canJump([2,5,0,0]) # expect True
print test.canJump(
[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
)