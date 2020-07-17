class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        self.d = {0:1, 1:x}
        if n > 0:
            return self.calcPow(x, n)
        else:
            return 1./self.calcPow(x, -n)

    def calcPow(self, x, n):
        if self.d.get(n) is not None:
            return self.d.get(n)
        if n % 2 == 0:
            res = self.calcPow(x, n/2)*self.calcPow(x, n/2)
        else:
            res = self.calcPow(x, n/2)*self.calcPow(x, n/2)*x
        self.d[n] = res
        return res

test = Solution()
print test.myPow(2.00000, 10) # 1024.00000
print test.myPow(2.10000, 3) # 9.26100
print test.myPow(2.00000, -2) # 0.25



