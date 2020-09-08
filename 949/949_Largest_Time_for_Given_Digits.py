class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        s = ''
        for hour in range(23, -1, -1):
            minute_arr = A[:]
            str_hour = str(hour)
            if hour < 10:
                str_hour = '0' + str_hour
            is_hour_possible = True
            for char in str_hour:
                if int(char) not in minute_arr:
                    is_hour_possible = False
                    break
                minute_arr.remove(int(char))
            if not is_hour_possible:
                continue
            minuate_a = minute_arr[0]*10 + minute_arr[1]
            minuate_b = minute_arr[1]*10 + minute_arr[0]
            minute_max = max(minuate_a, minuate_b)
            minute_min = min(minuate_a, minuate_b)
            if self.isValidMinute(minute_max):
                str_minute = str(minute_max)
                if minute_max < 10:
                    str_minute = '0' + str_minute
                return str_hour + ':' + str_minute
            elif self.isValidMinute(minute_min):
                str_minute = str(minute_min)
                if minute_min < 10:
                    str_minute = '0' + str_minute
                return str_hour + ':' + str_minute
        return s

    def isValidHour(self, s):
        return int(s) >= 0 and int(s) < 23

    def isValidMinute(self, s):
        return int(s) >= 0 and int(s) < 60


test = Solution()
print test.largestTimeFromDigits([1,2,3,4])
print test.largestTimeFromDigits([5,5,5,5])
print test.largestTimeFromDigits([0,0,0,0])