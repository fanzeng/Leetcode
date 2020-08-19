class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        self.N = N
        self.K = K
        self.res = []
        if self.N == 1:
            self.res.append(0)
        for digit in xrange(1,10):
            self.expand(digit)
        return sorted(list(set(self.res)))

    def expand(self, num):
        if len(str(num)) < self.N:
            l_next_digit = self.nextDigit(int(str(num)[-1]))
            for chiffre in l_next_digit:
                new_num = num * 10 + chiffre
                # print new_num
                self.expand(new_num)
        else:
            self.res.append(num)

    def nextDigit(self, digit):
        l_next_digit = []
        if digit - self.K >= 0:
            l_next_digit.append(digit - self.K)
        if digit + self.K < 10:
            l_next_digit.append(digit + self.K)
        return l_next_digit

test = Solution()
print test.numsSameConsecDiff(3, 7) # [181,292,707,818,929]
print test.numsSameConsecDiff(2, 1) # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
print test.numsSameConsecDiff(1, 0) # [0,1,2,3,4,5,6,7,8,9]
print test.numsSameConsecDiff(2, 0) # [11,22,33,44,55,66,77,88,99]