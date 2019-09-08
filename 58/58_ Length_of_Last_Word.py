class Solution(object):
	def lengthOfLastWord(self, s):
		sp = s.strip().split(' ')
		if sp[-1] is not None:
			return len(sp[-1])
		else:
			return 0