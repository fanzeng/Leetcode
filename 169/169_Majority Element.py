class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if d.get(num) is None:
                d[num] = 1
            else:
                d[num] += 1
            if d[num] > len(nums)/2:
                return num

test = Solution()
print test.majorityElement([3,2,3]) # 3
print test.majorityElement([2,2,1,1,1,2,2]) # 2