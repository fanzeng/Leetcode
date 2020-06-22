class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.d = {}
        for num in nums:
            if self.d.get(num) is None:
                self.d[num] = 1
            else:
                self.d[num] += 1
        for key, val in self.d.items():
            if val == 1:
                return key