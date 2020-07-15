class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        ang_min = minutes/60.*360
        ang_hour = (hour%12)/12.*360 + minutes/60.*30
        diff = abs(ang_min - ang_hour)
        return diff if diff < 180 else 360-diff

test = Solution()
print test.angleClock(12, 30) # 165
print test.angleClock(3, 30) # 75
print test.angleClock(3, 15) # 7.5
print test.angleClock(4, 50) # 155
print test.angleClock(12, 0) # 0