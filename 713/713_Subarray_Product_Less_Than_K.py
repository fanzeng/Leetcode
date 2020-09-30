class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        start = 0
        prod = nums[0]
        end = start + 1
        while start < len(nums):
            while True:
                if end <= start:
                    prod = nums[start]
                    end = start + 1
                # print start, end, prod, count
                if prod >= k:
                    end -= 1
                    prod /= nums[end]
                    count += max(0, end - start)
                    break
                elif end == len(nums):
                    count += end - start
                    break
                if end < len(nums):
                    prod *= nums[end]
                    end += 1

            prod /= nums[start]
            start += 1
        return count

test = Solution()
print test.numSubarrayProductLessThanK([10,5,2, 6], 100) # 8
print test.numSubarrayProductLessThanK([1,2,3], 0) # 0
print test.numSubarrayProductLessThanK([1,1,1,8,1,1,1], 5) # 12
print test.numSubarrayProductLessThanK([1,1,1,8,1,8,1,1,1], 5) # 13

