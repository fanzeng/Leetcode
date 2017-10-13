class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		if len(needle) < 1:
			return 0
		elif len(haystack) < 1:
			return -1
		for i in range(len(haystack)-len(needle)+1):
			for j in range(len(needle)):
				if haystack[i+j] != needle[j]:
					break
			if j == len(needle)-1 and haystack[i+j] == needle[j]:
				return i
		return -1


test = Solution()
print test.strStr('abc', 'ab')
print test.strStr('abc', 'bc')
print test.strStr('abc', 'c')
print test.strStr('abc', 'cd')
print test.strStr('abc', 'd')
print test.strStr('abc', '')
print test.strStr('', '')