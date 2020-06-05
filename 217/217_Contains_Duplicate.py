class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            if d.get(n) is not None:
                return True
            else:
                d[n] = 1
        return False
test = Solution()
print test.containsDuplicate([1,2,3,1]) # True
print test.containsDuplicate([1,2,3,4]) # False
print test.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) # True