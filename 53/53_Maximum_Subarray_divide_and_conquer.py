class Solution(object):
	def get_max_sub_array_across(self, nums, mid):
		max_l_pos = mid
		max_r_pos = mid+1
		max_sum_l = 0
		sum_l = 0

		for l in range(mid-1, -1, -1):
			sum_l += nums[l]
			if sum_l > max_sum_l:
				max_sum_l = sum_l
				max_l_pos = l

		max_sum_r = 0
		sum_r = 0
		for r in range(mid+1, len(nums)):
			sum_r += nums[r]
			if sum_r > max_sum_r:
				max_sum_r = sum_r
				max_r_pos = r

		return nums[mid] + max_sum_l + max_sum_r, max_l_pos, max_r_pos

	def get_max_sub_array(self, nums):
		if len(nums) == 1:
			max_sum = nums[0]
			start_pos = 0
			end_pos = 1
		else:
			mid = len(nums)/2
			max_sum_l, start_pos_l, end_pos_l = self.get_max_sub_array(nums[:mid])
			max_sum_r, start_pos_r, end_pos_r = self.get_max_sub_array(nums[mid:])
			# start_pos_across = start_pos_l
			# end_pos_across = mid + end_pos_r
			# sum_across = sum(nums[start_pos_across:end_pos_across])
			max_sum_across, start_pos_across_, end_pos_across_ = \
				self.get_max_sub_array_across(nums[start_pos_l:mid+end_pos_r+1], mid-start_pos_l)
			start_pos_across = start_pos_l + start_pos_across_
			end_pos_across = start_pos_l + end_pos_across_

			if max_sum_l >= max_sum_r and max_sum_l >= max_sum_across:
				max_sum = max_sum_l
				start_pos = start_pos_l
				end_pos = end_pos_l
			elif max_sum_r > max_sum_l and max_sum_r >= max_sum_across:
				max_sum = max_sum_r
				start_pos = mid + start_pos_r
				end_pos = mid + end_pos_r
			else:
				max_sum = max_sum_across
				start_pos = start_pos_across
				end_pos = end_pos_across
		return max_sum, start_pos, end_pos

	def maxSubArray(self, nums):
		max_sum, start_pos, end_pos = self.get_max_sub_array(nums)
		return max_sum, 'start_pos = ' + str(start_pos) + ', end_pos = ' + str(end_pos)

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
	res, info = test.maxSubArray(test_in)

	if res != ans:
		print test_in, res, '!=', ans
		print info

do_test(list_test)