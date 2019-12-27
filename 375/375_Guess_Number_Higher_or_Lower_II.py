class Solution(object):
	def __init__(self):
		self.dictRes = {}

	def getMoneyAmount(self, n):
		return self.getMoneyAmountDP(1, n)


	def getMoneyAmountDP(self, lo, hi):
		gap = hi - lo
		if gap <= 0:
			res = 0
		elif gap == 1:
			res = lo
		elif gap == 2:
			res = lo + 1
		else:
			dictTrial = self.dictRes.get((lo, hi))
			if dictTrial is not None:
				res = dictTrial
			else:
				guess = lo
				res = guess + self.getMoneyAmountDP(guess + 1, hi)
				for guess in range(lo+1, hi):
					maxLoss = max(self.getMoneyAmountDP(guess + 1, hi), self.getMoneyAmountDP(lo, guess - 1))
					res = min(res, guess + maxLoss)
		self.dictRes[(lo, hi)] = res
		return res

def doTest(n):
	test = Solution()
	print 'n =', n, ', result =', test.getMoneyAmount(i)

if __name__ == '__main__':
	for i in range(10):
		doTest(i)
