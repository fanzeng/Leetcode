class Solution(object):
	def maxSubArray(self, nums):
		'''
		The max subarray starts from one of the all possible
		positions:
		0, 1, ... , len(nums)-1
		A for loop goes through these possible starting positions,
		and greedily changing to start from i if doing so gives a
		larger sum_since_reset.
		All possible ending positions are dealt with by storing
		all time maximum of sum_since_reset in max_sum.
		'''
		if len(nums) == 1:
			return nums[0]
		else:
			sum_since_reset = nums[0]
			max_sum = sum_since_reset
			for i in range(1,len(nums)):
				sum_since_reset += nums[i]
				if nums[i] > sum_since_reset:
					sum_since_reset = nums[i]
				max_sum = max(max_sum, sum_since_reset)
			return max_sum

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
([3,-4,2,-3],3),
([-3,3,3,3,2,3],14)
]
def do_test(list_test):
	for t in list_test:
		test_in, ans = t
		test(test_in, ans)

def test(test_in, ans):
	test = Solution()
	res = test.maxSubArray(test_in)

	if res != ans:
		print test_in, res, '!=', ans

do_test(list_test)