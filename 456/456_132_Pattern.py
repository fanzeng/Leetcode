class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_no_repeat = []
        for num in nums:
            if len(nums_no_repeat) == 0 or num != nums_no_repeat[-1]:
                nums_no_repeat.append(num)
        nums = nums_no_repeat
        if len(nums) < 3:
            return False
        i = 1
        # go through nums with each num as candidate for "2"
        # let "3" be the rightmost position of numbers that are greater than num and on the left of num
        # let "1" be the leftmost position of numbers that are smaller than num and on the left of num
        # if leftmost_smaller < rightmost_greater, return True
        running_max = nums[0]
        running_min = nums[0]
        d_first_below = {nums[0]+1: 0}
        while i < len(nums):
            if nums[i] > running_max:
                running_max = nums[i]
                continue
            if nums[i] < running_min:
                running_min = nums[i]
                if d_first_below.get(nums[i]+1) is None:
                    d_first_below[nums[i]+1] = i
                continue

            j = i - 1
            greater = -1
            while j >= 0:
                if nums[j] > nums[i]:
                    greater = j
                    break
                j -= 1
            l_key = [key for key in d_first_below.keys() if key <= nums[i]]
            # print i, nums[i], d_first_below, l_key
            if len(l_key) > 0:
                k = min([d_first_below[key] for key in l_key])
                if k < greater:
                    return True
            i += 1
        return False

test = Solution()
print test.find132pattern([1,2,3,4]) # False
print test.find132pattern([1,1,1,1]) # False
print test.find132pattern([1,2,1,2]) # False
print test.find132pattern([1,2,1,3]) # False

print test.find132pattern([3,1,4,2]) # True
print test.find132pattern([-1,3,2,0]) # True
print test.find132pattern([1,4,0,-1,-2,-3,-1,-2]) # True
print test.find132pattern([3,5,0,3,4]) # True
print test.find132pattern([42,43,6,12,3,4,6,11,20]) # True