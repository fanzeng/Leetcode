class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		if divisor == 0:
			return 2147483647
		quotient = 0
		if ((dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0)):
			sign = 1
		else:
			sign = -1
		scale_factor = len(str(dividend))
		while scale_factor >= 0:
			while(quotient*abs(divisor) <= abs(dividend)):
				quotient += 10**scale_factor
			quotient -= 10**scale_factor
			scale_factor -= 1
		if quotient >= 2147483647:
			if sign == 1:
				return 2147483647
			else:
				return -2147483648
		if sign == 1:
			return quotient
		else:
			return -quotient
test = Solution()
print test.divide(-2147483648, -1)

