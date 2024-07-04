class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.d = {}
        return self.doJump(0)

    # def doJump(self, pos):
    #     if pos == len(self.nums) - 1:
    #         return 0
    #     if self.d.get(pos) is not None:
    #         return self.d[pos]
    #     m = 10001
    #     for j in range(pos + 1, min(len(self.nums), pos + self.nums[pos] + 1)):
    #         res = self.doJump(j)
    #         if res < m:
    #             m = res
    #     self.d[pos] = m + 1
    #     return m + 1
    
    def doJump(self, pos):
        res = [0]*len(self.nums)
        for pos in range(len(self.nums) - 2, -1, -1):
            end = min(len(res), pos + self.nums[pos] + 1)
            if pos + 1 == end:
                res[pos] = res[pos + 1] + 1
            else:
                res[pos] = min(res[pos + 1:end]) + 1
        # print res
        return res[0]
