class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}  # i -> (max_val_starting_from_i, index_of_the_max_val)
        i = len(nums) - 1
        maxi = nums[-1]
        j = len(nums) - 1
        while i > -1:
            if nums[i] > maxi:
                j = i
                maxi = nums[i]
            d[i] = [maxi, j]
            i -= 1
        w = 0
        i = 0
        j = 0
        # Increase j eagerly while increase i only when have to.
        # For any i, if there exists a num[j+x] to the right of j that's >= nums[i],
        # we don't want to increase i, because the interval between current i and j+x
        # is a ramp, and dominates any interval inside it, which we don't need to check.
        # On the other hand, if i and j is some distance apart,
        # That means we have a valid interval at least j-i in width
        # (otherwise we would've increased i and j together by our algo),
        # so we don't need to check any interval smaller than j-i by increasing i only.
        # Either way there is nothing to gain to increase i without increasing j.
        # So we can always increase j by 1 in every loop.
        while j < len(nums):
            while i < j and d[j][0] < nums[i]:
                i += 1
            w = max(w, j - i)
            j += 1 
        return w
