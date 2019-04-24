class Solution(object):
	def searchRange(self, nums, target):
		l = 0
		r = len(nums) - 1
		m = len(nums) / 2
		if len(nums) < 1:
			return -1, -1
		elif len(nums) == 1:
			if nums[0] != target:
				return -1, -1
			else:
				return 0, 0

		while (True):
			if l >= r - 1 and nums[l] != target and nums[r] != target:
				return -1, -1
			if nums[m] > target:
				r = m
				m = (l + m) / 2
			elif nums[m] < target:
				l = m
				m = (r + m + 1) / 2
			else:
				break
		# print 'l, m, r =', l, m, r
		rf = m
		lf = l
		mf = (lf + rf) / 2
		while not ((mf == 0 or nums[mf-1] < target) and nums[mf] == target):
			# print 'lf, mf, rf =', lf, mf, rf
			if (nums[mf] < target):
				lf = mf
				mf = (lf + rf + 1) / 2
			else:
				rf = mf
				mf = (lf + rf) / 2
		ans_f = mf

		ll = m
		rl = r
		ml = (ll + rl) / 2

		while not ((ml == len(nums)-1 or nums[ml+1] > target) and nums[ml] == target):
			if (nums[ml] > target):
				rl = ml
				ml = (ll + rl) / 2
			else:
				ll = ml
				ml = (ll + rl + 1) / 2
		ans_l = ml

		return ans_f, ans_l

test = Solution()
nums = [5,7,7,8,8,10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

nums = [5,7,7,7,7,8,8,8,8,8,10]
target = 7

# nums = [1,2,3]
# target = 3

# nums = [1,2,2]
# target = 2
print test.searchRange(nums, target)

