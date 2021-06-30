class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k >= len(nums):
            return [max(nums)]
        res = [max(nums[:k])]
        m = res[0]
        i = 0
        for num in nums[k:]:
            if num >= m:
                m = num
            elif nums[i] == m:
                m = max(nums[i+1:i+k+1])
            res.append(m)
            i += 1
        return res

test = Solution()
print test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) # [3,3,5,5,6,7]
print test.maxSlidingWindow([9,11], 2) # [11]
print test.maxSlidingWindow([4,-2], 2) # [4]
print test.maxSlidingWindow([7,2,4], 2) # [7,4]
print test.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5) # [10,10,9,2]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10], 3) # [10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10], 3) # [10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10]