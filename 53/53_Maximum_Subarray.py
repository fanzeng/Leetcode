class Solution(object):
	def maxSubArray(self, nums):
		info = ''
		if len(nums) == 1:
			return nums[0]
		# nums = nums + [-1]
		start = 0
		end = 0
		sum = 0
		sum_from_last_start = sum
		sum_from_last_end = 0
		for i in range(len(nums)):
			sum_from_last_start += nums[i]

			if i >= end:
				sum_from_last_end += nums[i]
			if sum < 0 and nums[i] > sum:
				sum = nums[i]
				start = i
				end = i + 1
				continue
			if (nums[i] < 0 and i < len(nums)-1 and nums[i+1] > sum):
				if sum_from_last_start <= 0:
					start = i + 1
					end = i + 2
					sum = nums[i + 1]
					sum_from_last_start = 0
					sum_from_last_end = 0

					info += 'i =' + str(i) + 'start =' + str(start) + ', end =' + str(end) + \
							', sum =' + str(sum) + ',' + str(sum_from_last_start) \
							+ ',' + str(sum_from_last_end)
					continue
			elif (nums[i] > 0 and i+1 < len(nums) and nums[i+1] < 0) or i+1==len(nums):
				if sum_from_last_end >= 0:
					end = i+1
					sum += sum_from_last_end
					sum_from_last_end = 0
					# if end == len(nums) - 1:
					# 	sum += nums[i]
				# print i, 'neg', len(nums)
			else:
				if end == 0:
					if nums[i] > 0 and nums[i+1] > 0:
						sum = nums[i] + nums[i+1]
						start = i
						end = i + 2
					elif nums[i] > nums[i+1]:
						sum = nums[i]
						start = i
						end = i + 1
					else:
						sum = nums[i+1]
						start = i+1
						end = i + 2
						if end >= len(nums):
							break
					sum_from_last_start = sum
					sum_from_last_end = 0
				# print i, 'do not care', nums[i], nums[i+1]

			info += 'i =' + str(i) + 'start =' + str(start) + ', end =' + str(end) + \
					', sum =' + str(sum) + ' ,' + str(sum_from_last_start) \
					+ ' ,' + str(sum_from_last_end)
		return sum, info
		return sum

list_test = [
([-2,1,-3,4,-1,2,1,-5,4],6),
([1,-1,-1,2],2),
([1,0,1,2],4),
([-2,1],1),
([-2,-1],-1),
([-1,-2],-1),
([-2,-3,-1],-1),
([1,2],3),
# ([2,1],3),
# ([1],1),
([-1],-1),
# ([8,-19,5,-4,20],21),
# ([2,-1,1,1],3),
# ([1,0,0,0],1),
([3,-4,2,-3],3)
]
def do_test(list_test):
	for t in list_test:
		test_in, ans = t
		test(test_in, ans)

def test(test_in, ans):
	if not isinstance(test_in, list):
		print 'not list'
		test_in = [test_in]
	test = Solution()
	info, res = test.maxSubArray(test_in)
	print test_in, 'ans =', ans

	if res != ans:
		print test_in, res, ' != ', ans
		print info

do_test(list_test)