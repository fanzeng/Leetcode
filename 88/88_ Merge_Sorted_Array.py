class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        merged = []
        while True:
            if i1 < m and (i2 == n or nums1[i1] <= nums2[i2]):
                merged.append(nums1[i1])
                i1 += 1
            elif i2 < n and (i1 == m or nums1[i1] > nums2[i2]):
                merged.append(nums2[i2])
                i2 += 1
            else:
                break

        for i in range(len(merged)):
            nums1[i] = merged[i]

test = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
test.merge(nums1, m, nums2, n)
print nums1

nums1 = [1,0]
m = 1
nums2 = [2]
n = 1
test.merge(nums1, m, nums2, n)
print nums1

nums1 = [5,6,0,0,0,0,0,0,0,0]
m = 2
nums2 = [1,2,3,4,7,8,9,10]
n = 8
test.merge(nums1, m, nums2, n)
print nums1
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]