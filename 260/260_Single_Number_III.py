class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        return list(s)
test = Solution()
print test.singleNumber([1,2,1,3,2,5]) # [3, 5] or [5, 3]