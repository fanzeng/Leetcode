class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 1:
            return None

        elif len(nums) % 2 == 0:
            print 'input array must have even length.'
            return None
        else:
            return self.singleNonDuplicateRecursive(nums)

    def singleNonDuplicateRecursive(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 3:
            if nums[0] == nums[1]:
                return nums[2]
            elif nums[1] == nums[2]:
                return nums[0]
        else:
            m = len(nums) / 2
            if m % 2 == 0:
                if nums[m] == nums[m-1]:
                    return self.singleNonDuplicateRecursive(nums[:m-1])
                elif nums[m] == nums[m+1]:
                    return self.singleNonDuplicateRecursive(nums[m+2:])
                else:
                    return nums[m]
        if m % 2 == 1:
            if nums[m] == nums[m+1]:
                return self.singleNonDuplicateRecursive(nums[:m])
            elif nums[m] == nums[m-1]:
                return self.singleNonDuplicateRecursive(nums[m+1:])
            else:
                return nums[m]


test = Solution()
print test.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) # 2
print test.singleNonDuplicate([3,3,7,7,10,11,11]) # 10