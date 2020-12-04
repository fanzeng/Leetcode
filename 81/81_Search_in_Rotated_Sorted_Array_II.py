class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target
        if nums[0] == nums[-1]:
            if nums[0] == target:
                return True
            else:
                nums = [n for n in nums if n != nums[0]]
                if len(nums) == 0:
                    return False
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[l]:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    if target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
            elif nums[mid] >= nums[r]:
                if target < nums[mid]:
                    if target < nums[l]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
        if nums[r] == target:
            return True
        else:
            return False

test = Solution()
print test.search([2,5,6,0,0,1,2], 0) # True
print test.search([1,1], 1) # True
print test.search([1,3,1,1,1], 3) # True
print test.search([2,5,6,0,0,1,2], 3) # False
print test.search([2,5,6,0,0,1,2], 3) # False
print test.search([], 5) # False
