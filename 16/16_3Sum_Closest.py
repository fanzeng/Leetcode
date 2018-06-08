class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		d = {}
		import sys
		best = sys.maxint
		current = 0
		for index_i, i in enumerate(nums):
			for index_j, j in enumerate(nums[index_i+1:]):
				d[i+j] = (index_i, index_i+1+index_j)
		# print d
		for index_i, i in enumerate(nums):
			for key in d.keys():
				current = i + key
				if abs(target - current) < abs(target - best) and index_i not in d[key]:
					best = current
					# print index_i, d[key]
		return best



test = Solution()
S = [-1, 0, 1, 2, -1, -4]
print test.threeSumClosest(S, -7)

S = [-1, 0, 1]
print test.threeSumClosest(S, 1)