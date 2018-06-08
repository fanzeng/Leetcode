class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		result = set()
		if n == 0:
			return None
		elif n == 1:
			return ['()']
		else:
			for n_minus_1_result in self.generateParenthesis(n-1):
				result.add('(' + n_minus_1_result  + ')')
				open = 0
				close = 0
				for i in range(len(n_minus_1_result)):
					if n_minus_1_result[i] == '(':
						open += 1
					else:
						close += 1
						if (open == close):
							result.add('(' + n_minus_1_result[:i+1] + ')' + n_minus_1_result[i+1:])

				result.add(n_minus_1_result + '()')
				result.add('()' + n_minus_1_result)
			return list(result)

test = Solution()
print test.generateParenthesis(2)
print test.generateParenthesis(3)
print test.generateParenthesis(4)
