class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            nums[abs(n)-1] *= -1
        # print nums
        res = []
        for i, n in enumerate(nums):
            if nums[abs(n)-1] > 0:
                res.append(abs(n))
        return list(set(res))

test = Solution()
print test.findDuplicates([4,3,2,7,8,2,3,1]) # 2, 3
print test.findDuplicates([2,2]) # 2
print test.findDuplicates([5,4,6,7,9,3,10,9,5,6]) # [5,6,9]