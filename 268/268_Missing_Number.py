class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist = [False]*(max(nums)+2)
        for num in nums:
            exist[num] = True
        for i, e in enumerate(exist):
            if not e:
                return i

test = Solution()
print test.missingNumber([3,0,1]) # 2
print test.missingNumber([9,6,4,2,3,5,7,0,1]) # 8