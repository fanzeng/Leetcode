class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.partialSum = []
        sum = 0
        for n in nums:
            sum += n
            self.partialSum.append(sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.partialSum[j]
        return self.partialSum[j] - self.partialSum[i-1]

obj = NumArray([-2,0,3,-5,2,-1])
print obj.sumRange(0,2) # 1
print obj.sumRange(2,5) # -1
print obj.sumRange(0,5) # -3