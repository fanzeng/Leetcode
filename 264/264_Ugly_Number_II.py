class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        n -= 1
        self.uglynumbers = {2, 3, 5}
        while True:
            smallest_new = self.expand()
            # print self.uglynumbers
            if len([x for x in self.uglynumbers if x < smallest_new]) > n:
                break
        return sorted(list(self.uglynumbers))[n-1]

    def expand(self):
        new = []
        for i in [2,3,5]:
            for j in self.uglynumbers:
                new.append(i*j)
        # print 'new =' , new
        smallest_new = min([x for x in new if x not in self.uglynumbers])
        self.uglynumbers.update(new)
        # print 'smallest new =', smallest_new
        return smallest_new

test = Solution()
print test.nthUglyNumber(10) # 12
print test.nthUglyNumber(27) # 64
print test.nthUglyNumber(100) # 1536