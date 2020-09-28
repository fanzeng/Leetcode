class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        poison_end_time = 0
        for time in timeSeries:
            total += duration - max(0, poison_end_time - time)
            poison_end_time = max(poison_end_time, time + duration)
        return total

test = Solution()
print test.findPoisonedDuration([1,4], 2) # 4
print test.findPoisonedDuration([1,2], 2) # 3

