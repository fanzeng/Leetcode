class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        set_composite = set()
        for i in xrange(2, n):
            if i in set_composite:
                continue
            sum = i
            while(sum+i < n):
                sum += i
                set_composite.add(sum)
            if i*i > n:
                break
        count = 0
        for i in xrange(2, n):
            if i not in set_composite:
                count += 1
        return count

test = Solution()
print  test.countPrimes(10) # 4
print  test.countPrimes(11) # 4
print  test.countPrimes(12) # 5