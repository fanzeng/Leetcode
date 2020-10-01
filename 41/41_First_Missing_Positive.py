class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        count_pos = len([n for n in nums if n > 0])
        set_nums = set(nums)
        for n in xrange(1, count_pos+1):
            if n not in set_nums:
                return n
        return count_pos + 1

test = Solution()
print test.firstMissingPositive([1,2,0]) # 3
print test.firstMissingPositive([3,4,-1,1]) # 2
print test.firstMissingPositive([7,8,9,11,12]) # 1
print test.firstMissingPositive([1]) # 2
print test.firstMissingPositive([2]) # 1