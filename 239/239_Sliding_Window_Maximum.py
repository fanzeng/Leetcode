class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums

        # test for special case: monotonic decreasing
        is_mono_desc = True
        for i in xrange(len(nums)-1):
            if nums[i+1] > nums[i]:
                is_mono_desc = False
                break
        if is_mono_desc:
            return nums[:-k+1]

        res = []
        current_max, current_max_id = self.getMaxAndLastMaxId(nums[:k])
        res.append(current_max)
        i = k
        while i < len(nums):
            if nums[i] >= current_max:
                current_max_id = i
                current_max = nums[i]
            else:
                if current_max_id == i-k:
                    current_max, current_max_id = self.getMaxAndLastMaxId(nums[i-k+1:i+1])
                    current_max_id += i-k+1
            res.append(current_max)
            i += 1
        return res

    def getMaxAndLastMaxId(self, nums):
        current_max = max(nums)
        current_max_id = max([id for id in xrange(len(nums)) if nums[id] == current_max])
        return current_max, current_max_id

test = Solution()
print test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) # [3,3,5,5,6,7]
print test.maxSlidingWindow([9,11], 2) # [11]
print test.maxSlidingWindow([4,-2], 2) # [4]
print test.maxSlidingWindow([7,2,4], 2) # [7,4]
print test.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5) # [10,10,9,2]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10], 3) # [10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10], 3) # [10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10]