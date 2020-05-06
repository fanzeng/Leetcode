class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) < 2:
            return
        count = 0
        src = 0
        start = src
        temp = nums[src]
        while count < len(nums):
            dst = (src+k)%len(nums)
            # swap(temp, nums[dst])
            temptemp = nums[dst]
            nums[dst] = temp
            temp = temptemp
            src = dst
            if src == start:
                src += 1
                start = src
                if src < len(nums):
                    temp = nums[src]
                else:
                    break
            count += 1
        return nums

    # def swap(self, a, b):
    #     temp = b
    #     b = a
    #     a = temp

test = Solution()
print test.rotate([1,2,3,4,5,6,7], 3) # [5,6,7,1,2,3,4]
print test.rotate([-1,-100,3,99], 2) # [3,99,-1,-100]
print test.rotate([1,2,3,4,5,6], 3) # [4,5,6,1,2,3]
print test.rotate([1,2], 3) # [2,1]
