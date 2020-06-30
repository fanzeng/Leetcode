class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = {1:1, 2:2, 3:3, 4:1}
        self.numSquaresDP(n)
        return self.d[n]


    def numSquaresDP(self, n):
        d_res = self.d.get(n)
        if d_res is not None:
            return d_res
        for i in xrange(5, n+1):
            l_res = []
            m = self.sqrtFloor(i)
            if m*m == i:
                self.d[i] = 1
                continue
            sq = m*m
            while sq > 0:
                # print i, i-sq
                r = 1 + self.d.get(i - sq)
                l_res.append(r)
                if r < 3:
                    break
                m -= 1
                sq = m*m
            # print i, l_res
            res = min(l_res)
            self.d[i] = res

    def sqrtFloor(self, n):
        m = 1
        while m*m <= n:
            m += 1
        return m - 1


test = Solution()
print test.numSquares(12) # 3
print test.numSquares(13) # 2
print test.numSquares(477) # 2
print test.numSquares(7168) # 4