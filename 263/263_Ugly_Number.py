class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num < 7:
            return True

        temp_num = num
        while temp_num % 2 == 0:
            temp_num /= 2
        while temp_num % 3 == 0:
            temp_num /= 3
        while temp_num % 5 == 0:
            temp_num /= 5
        return temp_num == 1

test = Solution()
print test.isUgly(8) # True
print test.isUgly(15) # True
print test.isUgly(18) # True
print test.isUgly(21) # False
print test.isUgly(22) # False
print test.isUgly(214797179)