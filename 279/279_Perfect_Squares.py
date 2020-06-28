class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = {1:1, 2:2, 3:3, 4:1}
        return self.numSquaresDP(n)


    def numSquaresDP(self, n):
        d_res = self.d.get(n)
        if d_res is not None:
            return d_res
        if self.is_sq(n):
            return 1
        l_res = []
        m = 1
        sq = m*m
        while n - sq >= n/2:
            r = 1 + self.numSquaresDP(n - sq)
            l_res.append(r)
            if r < 3:
                break
            m += 1
            sq = m*m
        # print n, l_res
        res = min(l_res)
        self.d[n] = res
        return res

    def is_sq(self, n):
        m = 1
        while m*m <= n:
            m += 1
        return (m-1)*(m-1) == n


test = Solution()
print test.numSquares(12) # 3
print test.numSquares(13) # 2
print test.numSquares(477) # 2
print test.numSquares(7168) # 2