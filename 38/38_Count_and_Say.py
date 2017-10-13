class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		s = '1'
		for i in range(1, n):
			s = self.say(s)
		return s

	def say(self, s):
		res = ''
		i = 0
		while i < len(s):
			j = 0
			while i+j<len(s) and s[i+j] == s[i]:
				j += 1
			res = res + str(j)+str(s[i])
			i = i + j
		return res

test = Solution()
print 'n=1:', test.countAndSay(1)
print 'n=2:', test.countAndSay(2)
print 'n=3:', test.countAndSay(3)
print 'n=4:', test.countAndSay(4)
print 'n=5:', test.countAndSay(5)
print 'n=6:', test.countAndSay(6)



