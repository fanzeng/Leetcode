class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2 and k == 1:
            return '12'
        if n == 2 and k == 2:
            return '21'
        fac_n_minus_one = self.factorial(n-1)
        permu = str((k-1) / fac_n_minus_one + 1)
        for c in list(self.getPermutation(n - 1, (k-1) % fac_n_minus_one + 1)):
            if int(c) < int(permu[0]):
                permu += str(int(c))
            else:
                permu += str(int(c)+1)

        return permu

    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n*self.factorial(n-1)

test = Solution()
print test.getPermutation(3, 3) # "213"
print test.getPermutation(3, 2) # "132"
print test.getPermutation(4, 9) # "2314"
