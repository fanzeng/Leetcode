class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		max_len = 0
		res = ''
		for i in range(len(s)):

			pal_len_1 = 0
			while i-pal_len_1>-1 and i+pal_len_1<len(s) and s[i-pal_len_1] == s[i+pal_len_1]:
				pal_len_1 += 1
			pal_len_1 -= 1
			if max_len < pal_len_1*2+1:
				max_len = pal_len_1*2+1
				res = s[i-pal_len_1:i+pal_len_1+1]

			pal_len_2 = 0
			while i-pal_len_2>-1 and i+pal_len_2<len(s)-1 and s[i-pal_len_2] == s[i+pal_len_2+1]:
				pal_len_2 += 1
			pal_len_2 -= 1
			if max_len < pal_len_2*2+2:
				max_len = pal_len_2*2+2
				res = s[i-pal_len_2:i+pal_len_2+2]
		return res


	# def is_Palindrome(self, s):
	# 	length = len(s)
	# 	for i in range(length/2):
	# 		if s[i] != s[length-1-i]:
	# 			return False
	# 	return True


test = Solution()
print test.longestPalindrome('aba')
print test.longestPalindrome('abbcdcbba')
print test.longestPalindrome('abbccbbae')
print test.longestPalindrome('abbccbba')
print test.longestPalindrome('cbba')