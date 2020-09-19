class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        s_nums2 = set(nums2)
        for num in set(nums1):
            if num in s_nums2:
                res.append(num)
        return res

test = Solution()
print test.intersection([1,2,2,1], [2,2]) # [2]
print test.intersection([4,9,5], [9,4,9,8,4]) # [9, 4]