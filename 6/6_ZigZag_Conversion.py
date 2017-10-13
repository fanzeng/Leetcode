class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows == 1:
			return s

		row = ['' for x in range(numRows)]
		r = 0
		direction = 1
		for i in range(len(s)):
			row[r]+=s[i]
			if r == numRows-1:
				direction = -1
			elif r == 0:
				direction = 1
			r += direction
		return ''.join(row)

test = Solution()
print test.convert('PAYPALISHIRING', 3)