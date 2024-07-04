class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        i = 0
        while i < len(nums):
            n = nums[i]
            if d.get(n) is not None:
                if d[n] < 2:
                    d[n] += 1
            else:
                d[n] = 1
            i += 1
        pos = 0
        for n in range(nums[0], nums[-1] + 1):
            if d.get(n) is not None:
                count = d[n]
                for i in range(count):
                    nums[pos] = n
                    pos += 1
        return pos
