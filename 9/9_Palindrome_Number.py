class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		x_str = str(x)
		if x_str[0] != x_str[-1]:
			return False
		i = 1
		while i < len(x_str)/2-1:
			if x_str[i] != x_str[-(i+1)]:
				return False
			i+=1
		return True

test = Solution()
print test.isPalindrome(1)
print test.isPalindrome(11)
print test.isPalindrome(121)
print test.isPalindrome(1231)
print test.isPalindrome(1210)
print test.isPalindrome(122133454331221)
print test.isPalindrome(122133454321221)

