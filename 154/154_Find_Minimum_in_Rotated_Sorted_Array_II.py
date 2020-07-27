class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        reverse_order = self.findReverseOrderDivideAndConquer(nums)
        if reverse_order is None:
            return nums[0]
        return nums[reverse_order+1]

    def findReverseOrderDivideAndConquer(self, nums):
        if len(nums) < 2:
            return None
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return None
        mid = len(nums)/2
        if nums[mid] > nums[mid+1]:
            return mid
        left = nums[:mid+1]
        right = nums[mid+1:]
        if left[0] >= left[-1]: # if this true, then the reverse order is likely in left, so try left first, otherwise try right first
            left_res = self.findReverseOrderDivideAndConquer(left)
            if left_res is not None: # if found, return directly
                return left_res
        right_res = self.findReverseOrderDivideAndConquer(right)
        if right_res is not None: # if found, return directly
            return mid + 1 + right_res
        if left[0] < left[-1]: # if left has not been calculated
            return self.findReverseOrderDivideAndConquer(left)
        else: # left has been calculated, but we are here so its result must be None
            return None

test = Solution()
print test.findMin([1]) # 1
print test.findMin([1,3]) # 1
print test.findMin([1,3,5]) # 1
print test.findMin([3,1,3,3]) # 1
print test.findMin([10,10,10,10,1]) # 1
print test.findMin([2,2,2,0,1]) # 0
print test.findMin([4,5,6,7,0,1,2]) # 0
print test.findMin([7,8,9,0,1,2,3,4,5,6]) # 0