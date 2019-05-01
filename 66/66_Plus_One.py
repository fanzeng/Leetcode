class Solution(object):
	def plusOne(self, digits):
		i = 0
		m = 1
		for d in digits[-1::-1]:
			i += m * d
			m *= 10
		i += 1
		ans = []
		m = 10
		while(i > 0):
			print 'i =', i
			ans.append((i % m)/(m/10))
			i -= ans[-1]*m/10
			m *= 10

		return ans[-1::-1]

test = Solution()
print test.plusOne([9,9,9,9])