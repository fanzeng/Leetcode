class Solution(object):
	def gen_str(self, letter_list):
		res = []
		if len(letter_list) == 1:
			for letter in letter_list[0]:
				res.append(letter)
			return res
		else:
			for letter in letter_list[0]:
				for rest in self.gen_str(letter_list[1:]):
					res.append(letter+rest)
			return res

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		d = {i:alphabet[3*(i-2):3*(i-1)] for i in range(2, 7)}
		d[7] = 'pqrs'
		d[8] = 'tuv'
		d[9] = 'wxzy'
		letter_list = []
		if len(digits) < 1:
			return []
		for i in range(len(digits)):
			letter_list.append(list(d.get(int(digits[i]))))
		res = self.gen_str(letter_list)
		return res

test = Solution()
print test.letterCombinations('2389')
print test.letterCombinations('')