class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perm = self.permute(nums)
        return [list(p) for p in set([tuple(p) for p in perm])]

    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[nums[0]]]
        perm = []
        n = nums[0]
        rest = self.permute(nums[1:])
        for arr in rest:
            for i in xrange(len(arr)+1):
                perm.append(self.insert(n, arr[:], i))
        return perm

    def insert(self, n, arr, i):
        return arr[:i] + [n] + arr[i:]

test = Solution()
print test.permuteUnique([1,1,2])