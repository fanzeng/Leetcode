class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if t == 0:
            d = {}
            for num in nums:
                if d.get(num) is None:
                    d[num] = True
                else:
                    return True
            return False
        shifted_nums = nums[:]
        for i in xrange(min([k, len(nums)])):
            shifted_nums = self.shiftLeft(shifted_nums)
            for j in xrange(len(nums)-i-1):
                diff = nums[j] - shifted_nums[j]
                if abs(diff) <= t:
                    return True
        return False

    def shiftLeft(self, nums):
        return nums[1:] + [nums[0]]

    def argmax(self, nums):
        max_nums = max(nums)
        return [item[0] for item in zip(xrange(len(nums)), nums) if item[1] == max_nums]

    def argmin(self, nums):
        min_nums = min(nums)
        return [item[0] for item in zip(xrange(len(nums)), nums) if item[1] == min_nums]

test = Solution()
print test.argmax([1,2,3,4,5])
print test.argmin([1,2,3,4,5])
print test.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) # True
print test.containsNearbyAlmostDuplicate([1,0,1,1,], 1, 2) # True
print test.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) # False
