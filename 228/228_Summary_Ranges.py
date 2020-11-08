class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums is None or len(nums) == 0:
            return []
        res = []
        nums.append(nums[-1])
        start = nums[0]
        prev = start
        i = 1
        while i < len(nums):
            if nums[i] > prev + 1 or i == len(nums)-1:
                end = prev
                if end == start:
                    res.append(str(start))
                    start = nums[i]
                    prev = start
                else:
                    res.append(str(start) + '->' + str(end))
                    start = nums[i]
                    prev = start
            else:
                prev = nums[i]
            i += 1
        return res

test = Solution()
print test.summaryRanges([0,1,2,4,5,7]) # ["0->2","4->5","7"]
print test.summaryRanges([0,2,3,4,6,8,9]) # ["0","2->4","6","8->9"]