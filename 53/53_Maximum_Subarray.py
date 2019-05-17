class Solution(object):
	def initialize(self, nums):
		self.start = 0
		self.end = 1
		self.sum = nums[0]
		self.sum_from_best_start = nums[0] # the accumulated sum from last best start (included) to num[i] (excluded)
		self.sum_from_best_end = nums[1] # the accumulated sum from last best end (included) to num[i] (excluded)
		self.nums = nums
		self.list_candidate_solution = []
		self.exist_positive = False

	def get_best_solution(self):
		best_solution_id = 0
		best_sum = self.list_candidate_solution[0].sum
		for solution_id, solution in enumerate(self.list_candidate_solution):
			if solution.sum  > best_sum:
				best_sum = solution.sum
				best_solution_id = solution_id
		return self.list_candidate_solution[best_solution_id]

	def record_candidate_solution(self):
		candidate_solution = CandidateSolution(self.start, self.end, self.sum)
		self.list_candidate_solution.append(candidate_solution)

	# Decide if an array index is a possible start to test for, start is included
	def is_possible_start(self, i):
		if i == 0:
			return True
		elif i >= len(self.nums):
			return False
		elif not self.exist_positive:
			return True
		elif self.nums[i] > 0 and self.nums[i-1] <= 0: # at this point the 2 array accesses should be valid
			return True


	# Decide if an array index is a possible end to test for, start is excluded
	def is_possible_end(self, i):
		if i == 0: # will not consider empty array
			return False
		elif i == len(self.nums):
			return True
		elif self.nums[i] < 0 and self.nums[i-1] >= 0: # at this point the 2 array accesses should be valid
			return True

	def decide_start_change(self, i):
		if self.sum_from_best_start < 0:
			if self.nums[i] < self.sum:
				self.record_candidate_solution()
			self.start = i
			self.end = i + 1
			self.sum = self.nums[i]
			self.sum_from_best_start = self.nums[i]
			if i + 1 < len(self.nums):
				self.sum_from_best_end = self.nums[i + 1]
			else:
				self.sum_from_best_end = 0
			return True
		else:
			return False

	def decide_end_change(self, i):
		if self.sum_from_best_end > 0:
			self.end = i
			self.sum += self.sum_from_best_end
			if i < len(self.nums):
				self.sum_from_best_start += self.nums[i]
				self.sum_from_best_end = self.nums[i]
			return True
		else:
			return False

	def maxSubArray(self, nums):
		info = ''
		if len(nums) == 1:
			return nums[0], ''
		self.initialize(nums)

		for i in range(len(nums)+1):
			if (not self.exist_positive) and i < len(nums) and nums[i] > 0:
				self.exist_positive = True
			changed = False
			if self.is_possible_start(i):
				changed = self.decide_start_change(i)
			elif self.is_possible_end(i):
				changed = self.decide_end_change(i)
			if not changed:
				if i > self.start and i < len(self.nums):
					self.sum_from_best_start += nums[i]
				if i > self.end and i < len(self.nums):
					self.sum_from_best_end += nums[i]
			info += self.get_info_string(i)

		self.record_candidate_solution()
		print 'begin'
		for s_id, s in enumerate(self.list_candidate_solution):
			print 'sol_id, start, end, sum = ', s_id, s.start, s.end, s.sum
		sol = self.get_best_solution()
		self.start = sol.start
		self.end = sol.end
		self.sum = sol.sum

		return self.sum, info
		return self.sum

	def get_info_string(self, i):
		return 'i=' + str(i) + ', start=' + str(self.start) + ', end=' + str(self.end) + \
		', sum=' + str(self.sum) + ', ' + str(self.sum_from_best_start) \
		+ ', ' + str(self.sum_from_best_end) + '\n'


class CandidateSolution():
	def __init__(self, start, end, sum):
		self.start = start
		self.end = end
		self.sum = sum

list_test = [
([-2,1,-3,4,-1,2,1,-5,4],6),
([1,-1,-1,2],2),
([1,0,1,2],4),
([-2,1],1),
([-2,-1],-1),
([-1,-2],-1),
([-2,-3,-1],-1),
([1,2],3),
([2,1],3),
([1],1),
([-1],-1),
([8,-19,5,-4,20],21),
([2,-1,1,1],3),
([1,0,0,0],1),
([3,-4,2,-3],3)
]
def do_test(list_test):
	for t in list_test:
		test_in, ans = t
		test(test_in, ans)

def test(test_in, ans):
	test = Solution()
	res, info = test.maxSubArray(test_in)

	if res != ans:
		print test_in, res, '!=', ans
		print info

do_test(list_test)