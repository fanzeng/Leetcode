class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        d = {}
        thresh = len(nums) / 3
        for num in nums:
            if d.get(num) is None:
                d[num] = 1
            else:
                d[num] += 1
        for k, v in d.items():
            if v > thresh:
                res.append(k)
        return res


test = Solution()
print test.majorityElement([3,2,3]) # [3]
print test.majorityElement([1]) # [1]
print test.majorityElement([1,2]) # [1,2]