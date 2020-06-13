class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        count_2 = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.insert(0, nums.pop(i))
            if nums[i] == 2:
                nums.append(nums.pop(i))
                count_2 += 1
                if i < len(nums)-1-count_2 or nums[i] == 0:
                    i -= 1
            i += 1
            # print i, nums
        return nums

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

test = Solution()
print test.sortColors([2,0,2,1,1,0]) # [0,0,1,1,2,2]
print test.sortColors([1,2,0]) # [0,1,2]
print test.sortColors([2,2,1]) # [1,2,2]