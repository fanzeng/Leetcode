class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        self.set_prime = set(range(2, n+1))
        self.l_factor = []
        while n > 1:
            p = self.set_prime.pop()
            n = self.tryPrime(n, p)
        print self.l_factor
        return self.l_factor[k] if k < len(self.l_factor) else -1
    
    def tryPrime(self, n, p):
        m = 2*p
        while m <= n:
            self.set_prime.discard(m)
            m += p
        if n % p == 0:
            self.l_factor.append(p)
        while n > 1 and n % p == 0:
            n /= p
        return n

test = Solution()
print test.kthFactor(12, 3)
print test.kthFactor(7, 2)
print test.kthFactor(4, 4) # -1
print test.kthFactor(1, 1)
print test.kthFactor(1000, 3)