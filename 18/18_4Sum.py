class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		if len(nums) < 4:
			return []
		from collections import defaultdict
		d2 = defaultdict(set)
		result = set()
		for index_i, i in enumerate(nums):
			for index_j, j in enumerate(nums[index_i + 1:]):
				d2[i + j].add(tuple(sorted([index_i, index_i + 1 + index_j])))
		# print d2
		temp = []
		for index_ii, ii in enumerate(d2.keys()):
			# print ii, jj, ':'
			# print d2.get(ii), d2.get(jj)
			jjj_list = d2.get(target - ii)
			if jjj_list != None:
				temp += [set(iii+jjj) for iii in d2.get(ii) for jjj in d2.get(target-ii)]
		for t in temp:
			if len(t)==4:
				result.add(tuple(sorted([nums[i] for i in t])))
		return list(result)

test = Solution()
# S = [-1, 0, -1, 2, -1, -4]
# print test.fourSum(S, -7)
# print test.fourSum(S, 0)

S = [1,0,-1,0,-2,2]
print test.fourSum(S, 0)
#
S = [-3,-2,-1,0,0,1,2,3]
print test.fourSum(S, 0)

S = [0,0,0,0]
print test.fourSum(S, 0)
