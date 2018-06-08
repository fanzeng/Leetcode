class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            id1 = -2
            while(nums[id1] >= nums[id1+1]): # Find the first occurrence of out-of-order element from the back
                id1 -= 1
                if id1 < -len(nums):
                    break
            # print 'id1 =', id1
            if id1 < -len(nums):
                nums.sort()
            else:
                id2 = -1
                while(nums[id2] <= nums[id1]):
                    id2 -= 1
                # print 'id2=', id2

                self.swap(nums, id1, id2)
                nums[id1+1:] = sorted(nums[id1+1:])

    def swap(self, nums, id1, id2):
        temp = nums[id1]
        nums[id1] = nums[id2]
        nums[id2] = temp


test = Solution()
# nums = [2]
# nums = [1, 2]
nums = [4, 1, 2, 5, 4, 3]
for i in range(1000):
    test.nextPermutation(nums)
    print nums