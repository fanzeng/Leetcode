class Solution(object):
	def deal_with_sick_case(self, nums2):
		if len(nums2) % 2 == 1:
			return nums2[len(nums2) / 2]
		else:
			return 0.5*(nums2[len(nums2) / 2] + nums2[len(nums2) / 2 - 1])

	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""

		if len(nums1) == 0:
			return self.deal_with_sick_case(nums2)
		if len(nums2) == 0:
			return self.deal_with_sick_case(nums1)


		i = 0
		j = 0
		total_len = len(nums1) + len(nums2)

		if nums1[0] < nums2[0]:
			move_which = 1
		else:
			move_which = 2
		count = 0
		if total_len % 2 == 1:
			while True:
				while (move_which == 1):
					i += 1
					count += 1
					result = nums1[i-1]
					# print '1: i =', i, ', j =', j, ', count =', count, ', included:', result
					if count > total_len / 2:
						return result
					if (i == len(nums1) or (j < len(nums2) and nums1[i] >= nums2[j])):
						move_which = 2


				while (move_which == 2):
					j += 1
					count += 1
					result = nums2[j-1]
					# print '2: i =', i, ', j =', j, ', count = ', count, ', included:', result
					if count > total_len / 2:
						return result
					if (j == len(nums2) or (i < len(nums1) and nums1[i] < nums2[j])):
						move_which = 1

		else:
			while True:
				while (move_which == 1):
					i += 1
					count += 1
					result = nums1[i-1]
					# print '1: i =', i, ', j =', j, ', count =', count, ', included:', result
					if count > total_len / 2:
						return 0.5*(result + last_result)
					last_result = result
					if (i == len(nums1) or (j < len(nums2) and nums1[i] >= nums2[j])):
						move_which = 2


				while (move_which == 2):
					j += 1
					count += 1
					result = nums2[j-1]
					# print '2: i =', i, ', j =', j, ', count = ', count, ', included:', result

					if count > total_len / 2:
						return 0.5*(result + last_result)
					last_result = result
					if (j == len(nums2) or (i < len(nums1) and nums1[i] < nums2[j])):
						move_which = 1
test = Solution()
# nums1 = [1, 2, 4, 6]
# nums2 = [3, 5, 7, 8]
# nums1 = [1, 2, 4, 6]
# nums2 = [3, 5, 7, 8, 9]
# nums1 = [1, 2]
# nums2 = [3, 4, 5]
# nums1 = [1]
# nums2 = [2]
# nums1 = []
# nums2 = [1, 2]
# nums1 = [1]
# nums2 = [2, 3, 4, 5]
# nums1 = [1, 2, 3]
# nums2 = [1, 2, 2]
# nums1 = [3]
# nums2 = [1, 2]
print test.findMedianSortedArrays(nums1, nums2)