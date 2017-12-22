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

# O(n^3) naive solution



# use twoSum hash table
# class Solution(object):
# 	def twoSum(self, nums, target):
# 		d = {}
# 		res = set()
# 		for num in nums:
# 			if num in d:
# 				res.add( tuple(sorted([num, d[num]])) )
# 			else:
# 				d[target - num] = num
# 		return res
#
#
# 	def threeSum(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: List[List[int]]
# 		"""
# 		res = set()
# 		for index, i in enumerate(nums):
# 			remain_1 = nums[:index]+nums[index+1:]
# 			twoSum_i = self.twoSum(remain_1, -i)
# 			for jk in twoSum_i:
# 				j, k = jk
# 				# print i, j, k
# 				res.add(tuple(sorted([i,j,k])))
# 		return [list(sol) for sol in res]
# use twoSum hash table



class Solution(object):
	def twoSum(self, nums, target):
		d = {}
		res = set()
		for num in nums:
			if num in d:
				res.add( tuple([num, d[num]]) )
			else:
				d[target - num] = num
		return res


	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = set()
		d = {}
		for index, i in enumerate(nums):
			if i in d:
				continue
			else:
				remain_1 = nums[index+1:]
				twoSum_i = self.twoSum(remain_1, -i)
				d[i] = twoSum_i
			for jk in twoSum_i:
				j, k = jk
				# print i, j, k
				res.add(tuple(sorted([i,j,k])))
		# print d
		return [list(sol) for sol in res]



S = [-1, 0, 1, 2, -1, -4]
test = Solution()
print test.twoSum(S, -2)
print test.threeSum(S)