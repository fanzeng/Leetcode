# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
	def firstBadVersion(self, n):
		if n <= 1:
			return 1
		l = 0
		r = n
		m = (l + r) / 2
		while (isBadVersion(m)):
			r = m
			m = (l + r) / 2
		# at this point, m is a good version, r is a bad version
		l = m
		m = (l + r) / 2
		while(l < r - 1):
			if isBadVersion(m):
				r = m
				m = (l + r) / 2
			else:
				l = m
				m = (l + r) / 2
		return m + 1


def isBadVersion(n):
	if n >= 5:
		return True
	else:
		return False

test = Solution()
print test.firstBadVersion(10)
print test.firstBadVersion(20)
print test.firstBadVersion(30)
print test.firstBadVersion(11)

