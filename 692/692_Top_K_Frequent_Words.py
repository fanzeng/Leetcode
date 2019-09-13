class Node(object):
	def __init__(self, word, count):
		self.word = word
		self.count = count

	def __str__(self):
		return self.word + ":" + str(self.count)

	def larger_than(self, other):
		if self.count > other.count:
			return True
		if self.count < other.count:
			return False
		elif self.word < other.word:
			return True
		else:
			return False

class MaxPQ(object):
	def __init__(self):
		self.heap = []

	def __str__(self):
		s = 'MaxPQ object:\n'
		for i, node in enumerate(self.heap):
			s += str(i) + ':' + str(node) + '\n'
		return s

	def size(self):
		return len(self.heap)

	def get_parent_pos(self, i):
		return (i-1)/2

	def get_right_son_pos(self, i):
		return (i+1)*2

	def get_left_son_pos(self, i):
		return (i+1)*2-1

	def enqueue(self, node):
		self.heap.append(node)
		i = self.size()-1
		while i > 0:
			current_node = self.heap[i]
			parent_pos =  self.get_parent_pos(i)
			parent = self.heap[parent_pos]

			if (current_node.larger_than(parent)):
				self.swap(i, parent_pos)
			i = parent_pos

	def swap(self, i, j):
		temp_node = Node(self.heap[i].word, self.heap[i].count)
		self.heap[i] = self.heap[j]
		self.heap[j] = temp_node

	def extract_max(self):
		self.swap(0, self.size()-1)
		max_node = self.heap.pop()
		i = 0
		while self.get_left_son_pos(i) < self.size():
			current_node = self.heap[i]
			left_son_pos = self.get_left_son_pos(i)
			left_son = self.heap[left_son_pos]
			if self.get_right_son_pos(i) < self.size():
				right_son_pos = self.get_right_son_pos(i)
				right_son = self.heap[right_son_pos]
			else:
				right_son = None
			if left_son.larger_than(current_node) or (right_son is not None and right_son.larger_than(current_node)):
				larger_son_pos = left_son_pos
				if right_son is not None and right_son.larger_than(left_son):
					larger_son_pos = right_son_pos
				self.swap(i, larger_son_pos)
				i = larger_son_pos
			else:
				break
			# print self

		return max_node

class Solution(object):

	def __init__(self):
		self.dict_word_count = {}

	def add_word_to_dict(self, word):
		if word in self.dict_word_count.keys():
			self.dict_word_count[word] += 1
		else:
			self.dict_word_count[word] = 1

	def topKFrequent(self, words, k):
		self.dict_word_count = {}
		for word in words:
			self.add_word_to_dict(word)
		print 'self.dict_word_count=', self.dict_word_count

		maxpq = MaxPQ()

		for key, val in self.dict_word_count.items():
			node = Node(key, val)
			maxpq.enqueue(node)
		res = []
		# print maxpq
		for i in range(k):
			res.append(maxpq.extract_max().word)
		return res

test = Solution()


# input_data_1 = (["i", "love", "leetcode", "i", "love", "coding"], 2)
# print 'Output should be: ["i", "love"]'
# print 'Ouput is: ', test.topKFrequent(*input_data_1)
#
# input_data_2 = (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
# print 'Ouput is: ', test.topKFrequent(*input_data_2)
# print 'Output should be: ["the", "is", "sunny", "day"]'
#
# input_data_3 = (["love", "leetcode", "love", "i", "i", "coding"], 2)
# print 'Output should be: ["i", "love"]'
# print 'Ouput is: ', test.topKFrequent(*input_data_3)
#
# input_data_4 = (["i", "love", "leetcode", "i", "love", "coding"], 3)
# print 'Output should be: ["i","love","coding"]'
# print 'Ouput is: ', test.topKFrequent(*input_data_4)

input_data_5 = (["glarko","zlfiwwb","nsfspyox","pwqvwmlgri","qggx","qrkgmliewc","zskaqzwo","zskaqzwo","ijy","htpvnmozay","jqrlad","ccjel","qrkgmliewc","qkjzgws","fqizrrnmif","jqrlad","nbuorw","qrkgmliewc","htpvnmozay","nftk","glarko","hdemkfr","axyak","hdemkfr","nsfspyox","nsfspyox","qrkgmliewc","nftk","nftk","ccjel","qrkgmliewc","ocgjsu","ijy","glarko","nbuorw","nsfspyox","qkjzgws","qkjzgws","fqizrrnmif","pwqvwmlgri","nftk","qrkgmliewc","jqrlad","nftk","zskaqzwo","glarko","nsfspyox","zlfiwwb","hwlvqgkdbo","htpvnmozay","nsfspyox","zskaqzwo","htpvnmozay","zskaqzwo","nbuorw","qkjzgws","zlfiwwb","pwqvwmlgri","zskaqzwo","qengse","glarko","qkjzgws","pwqvwmlgri","fqizrrnmif","nbuorw","nftk","ijy","hdemkfr","nftk","qkjzgws","jqrlad","nftk","ccjel","qggx","ijy","qengse","nftk","htpvnmozay","qengse","eonrg","qengse","fqizrrnmif","hwlvqgkdbo","qengse","qengse","qggx","qkjzgws","qggx","pwqvwmlgri","htpvnmozay","qrkgmliewc","qengse","fqizrrnmif","qkjzgws","qengse","nftk","htpvnmozay","qggx","zlfiwwb","bwp","ocgjsu","qrkgmliewc","ccjel","hdemkfr","nsfspyox","hdemkfr","qggx","zlfiwwb","nsfspyox","ijy","qkjzgws","fqizrrnmif","qkjzgws","qrkgmliewc","glarko","hdemkfr","pwqvwmlgri"]
, 14)
print 'Output should be: ["nftk","qkjzgws","qrkgmliewc","nsfspyox","qengse","htpvnmozay","fqizrrnmif","glarko","hdemkfr","pwqvwmlgri","qggx","zskaqzwo","ijy","zlfiwwb"]'
print 'Ouput is: ', test.topKFrequent(*input_data_5)
