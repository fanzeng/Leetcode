# class Solution(object):
# 	def maxArea(self, height):
# 		"""
# 		:type height: List[int]
# 		:rtype: int
# 		"""
#
# 		max_water = 0
# 		for id_first, first in enumerate(height):
# 			for id_second, second in enumerate(height[id_first+1:], id_first+1):
# 				water = min(second, first)*(id_second - id_first)
# 				if max_water < water:
# 					max_water = water
# 					# sol_first = id_first
# 					# sol_second = id_second
# 		return max_water



class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		max_water = 0
		id_first = 0
		id_second = len(height)-1
		while id_second>id_first:
			water = self.get_water(height, id_first, id_second)
			if water > max_water:
				max_water = water
			if height[id_second] > height[id_first]:
				id_first += 1
			else:
				id_second -= 1
		return max_water

	def get_water(self, height, id_first, id_second):
		return min(height[id_second], height[id_first])*(id_second-id_first)

test = Solution()
print test.maxArea([1, 5, 3, 4])
print test.maxArea([1, 1])