class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        d_count_1 = self.getCount(nums1)
        d_count_2 = self.getCount(nums2)
        for num in d_count_1.keys():
            count_2 = d_count_2.get(num)
            if count_2 is not None:
                count = min(d_count_1[num], count_2)
                for i in xrange(count):
                    res.append(num)
        return res

    def getCount(self, nums):
        d_count = {}
        for num in nums:
            if d_count.get(num) is None:
                d_count[num] = 1
            else:
                d_count[num] += 1
        return d_count

test = Solution()
print test.intersect([1,2,2,1], [2,2]) # [2,2]
print test.intersect([4,9,5], [9,4,9,8,4]) # [4,9]
