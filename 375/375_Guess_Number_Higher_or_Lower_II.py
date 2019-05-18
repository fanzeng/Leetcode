class Solution(object):
	def getMoneyAmount(self, n):
		if n == 1:
			return 0
		elif n == 2:
			return 1
		elif n == 3:
			return 2
		else:

strat = {}
strat[1] = 0
strat[2] = 1
def getStrategyDP(l, r):
	if strat.get([r - 1]) is not None:
		strat[n] = min(1 + )
	if r - l == 1:
		return l
	elif r - l == 2:
		return l + 1
	else:
		return min(l + strat)
# 		sum = 0
# 		if n == 1:
# 			return 0
# 		l = 1
# 		r = n
# 		m = (l + r) / 2
#
# 		while (l < r):
# 			print 'm =', m
# 			g = guess(m, n)
# 			sum += m
# 			if g == 0 or m == n - 1:
# 				break
# 			elif g > 0:
# 				l = m
# 				if m != n - 2:
# 					r += 1
# 					m = (l + r) / 2
# 				else:
# 					m = n -1
# 			else:
# 				r = m
# 				m = (l + r) / 2
# 		return sum
#
# def guess(num, ans):
# 	if num > ans:
# 		return -1
# 	elif num < ans:
# 		return 1
# 	else:
# 		return 0
# strategy = {}
# strategy[1] = 0
# strategy[2] = 0
# strategy[3] = 1
# strategy[4] =
# def get_strategy(l, r):
# 	return l + strategy[r - l]
test = Solution()
print test.getMoneyAmount(10)