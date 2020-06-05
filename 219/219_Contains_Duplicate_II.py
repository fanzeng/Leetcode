class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, n in enumerate(nums):
            if d.get(n) is not None and abs(d.get(n)-i) <= k:
                return True
            else:
                d[n] = i
        return False
test = Solution()
print test.containsNearbyDuplicate([1,2,3,1], 3) # True
print test.containsNearbyDuplicate([1,0,1,1], 1) # True
print test.containsNearbyDuplicate([1,2,3,1,2,3], 2) # False