class Solution(object):
	def canJump(self, nums):
		if min(nums) > 0:
			return True
		can_jump_result = [None] * len(nums)
		can_jump_result[-1] = True
		last_can_jump_pos = len(nums) - 1
		for i in range(len(nums)-2, -1, -1):
			jump_step = nums[i]
			if i + jump_step > len(nums)-1:
				can_jump_result[i] = True
				last_can_jump_pos = i
				continue
			else:
				# key realization here to prevent TLE:
				# if we start from the end, and keep track of the leftmost True
				# position, then we don't need to check every element within
				# step length, resulting in O(n) instead of O(n^2)
				if jump_step > 0 and i + jump_step + 1 > last_can_jump_pos:
					can_jump_result[i] = True
					last_can_jump_pos = i
					continue
				else:
					can_jump_result[i] = False
		return can_jump_result[0]

test = Solution()
print test.canJump([2,3,1,1,4]) # expect True
print test.canJump([3,2,1,0,4]) # expect False
print test.canJump([2,5,0,0]) # expect True
print test.canJump(
[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
) # expect False
print test.canJump([2,0,0]) # expect True