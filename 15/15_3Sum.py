# O(n^3) naive solution

# class Solution(object):
# 	def threeSum(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		res = set()
# 		for index, i in enumerate(nums):
# 			remain_1 =  nums[:index]+nums[index+1:]
# 			for index, j in enumerate(remain_1):
# 				remain_2 = remain_1[:index]+remain_1[index+1:]
# 				for k in remain_2:
# 					if i+j+k == 0:
# 						res.add(tuple(sorted([i,j,k])))
# 		return [list(sol) for sol in res]


class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = set()
		for index, i in enumerate(nums):
			remain_1 =  nums[:index]+nums[index+1:]
			for index, j in enumerate(remain_1):
				remain_2 = remain_1[:index]+remain_1[index+1:]
				for k in remain_2:
					if i+j+k == 0:
						res.add(tuple(sorted([i,j,k])))
		return [list(sol) for sol in res]





S = [-1, 0, 1, 2, -1, -4]
test = Solution()
print test.threeSum(S)