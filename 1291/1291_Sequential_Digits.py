class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        num_digit_low = self.getNumDigit(low)
        num_digit_high = self.getNumDigit(high)
        # print num_digit_low, num_digit_high
        all_seq_digit = []
        for num_digit in xrange(num_digit_low, num_digit_high+1):
            all_seq_digit += self.getSeqDigit(num_digit)
        return [x for x in all_seq_digit if x >= low and x <= high]

    def getNumDigit(self, a):
        return len(str(a))

    def getSeqDigit(self, n):
        l_seq_digit = []
        start = 1
        end = start + n
        while end <= 10:
            l_seq_digit.append(int(''.join([str(x) for x in range(start, end)])))
            start += 1
            end += 1
        return l_seq_digit

test = Solution()
print test.sequentialDigits(100, 300) # [123,234]
print test.sequentialDigits(1000, 13000) # [1234,2345,3456,4567,5678,6789,12345]