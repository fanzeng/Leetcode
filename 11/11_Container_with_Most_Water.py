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

'''
Proof:
Prove by contradiction:
Suppose we missed to check the correct answer, which is an interval with the largest possible area.
Since our left and right cursors must meet when we exit the program, the two edges of the correct answer must have been visited by those cursors.
It is either the left cursor visits the left edge first, or the right cursor visits the right edge first.
WLOG, assume the left cursor visits the left edge first.
Since we missed the correct answer, the left cursor must have moved right before the right cursor reached the right edge.
This means, there is an interval with width larger than correct answer, one edge at the left cursor, and the height at left cursor is the smaller one (because we moved the left cursor).
This wider interval is larger in area than the correct answer, because the height of the correct answer must be <= height of the common left edge.
Contradicts with the fact the correct answer has the largest area.


'''
