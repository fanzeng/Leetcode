class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while True:
            happy_value = self.happyProcess(n)
            # print 'happy value =', happy_value
            if happy_value == 1:
                return True
            elif happy_value in l:
                return False
            l.append(happy_value)
            n = happy_value
        return  False

    def happyProcess(self, n):
        sum = 0
        for c in str(n):
            sum += int(c)*int(c)
        return sum

test = Solution()
print test.isHappy(19)
print test.isHappy(1999)