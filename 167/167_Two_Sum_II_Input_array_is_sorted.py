class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(numbers):
            if d.get(num) is not None:
                return d.get(num)+1, i+1
            else:
                d[target-num] = i

test = Solution()
print test.twoSum([2,7,11,15], 9)