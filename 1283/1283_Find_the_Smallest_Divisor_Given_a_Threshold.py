class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        sum_nums = sum(nums)
        divisor_low = max(1, sum_nums/threshold)
        divisor_high = sum_nums
        divisor_mid = (divisor_low + divisor_high) / 2
        while divisor_low + 1 < divisor_high:
            s = self.getSum(nums, divisor_mid)
            # print 'divisor_mid =', divisor_mid, 's =', s
            if s == threshold:
                break
            if s < threshold:
                divisor_high = divisor_mid - 1
            else:
                divisor_low = divisor_mid + 1
            divisor_mid = (divisor_low + divisor_high) /2
        divisor = divisor_low
        while self.getSum(nums, divisor) > threshold:
            divisor += 1
        return divisor

    def getSum(self, nums, divisor):
        import math
        sum = 0
        for num in nums:
            sum += math.ceil(num*1.0/divisor)
        return sum

test = Solution()
print test.smallestDivisor([1,2,5,9], 6) # 5
print test.smallestDivisor([2,3,5,7,11], 11) # 3
print test.smallestDivisor([19], 5) # 4
print test.smallestDivisor([962551,933661,905225,923035,990560], 10) # 495280