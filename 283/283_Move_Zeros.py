class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero_locs = []
        while i < len(nums):
            if nums[i] != 0:
                if len(zero_locs) > 0:
                    nums[zero_locs[0]] = nums[i]
                    nums[i] = 0
                    zero_locs.pop(0)
                    zero_locs.append(i)

            else:
                zero_locs.append(i)
            i += 1
        return nums

test = Solution()
print test.moveZeroes([1]) # [1]
print test.moveZeroes([0]) # [0]
print test.moveZeroes([0, 1]) # [1, 0]
print test.moveZeroes([1, 0]) # [1, 0]
print test.moveZeroes([0, 1, 0, 3, 12]) # [1, 3, 12, 0, 0]
print test.moveZeroes([1, 0, 2, 0, 0, 0, 0, 1, 0, 3, 12]) # [1, 2, 1, 3, 12, 0, 0, 0, 0, 0, 0]
print test.moveZeroes([0, 0, 0, 0, 0, 1, 0, 3, 12, 0, 0, 0, 0, 0]) # [1, 3, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
