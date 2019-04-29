# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
	def guessNumber(self, n):
		if n == 1:
			return 1
		l = 0
		r = n + 1
		m = (l + r) / 2
		while(l < r):
			g = guess(m)
			if g == 0:
				return m
			elif g > 0:
				l = m
				m = (l + r) / 2
			else:
				r = m
				m = (l + r) / 2