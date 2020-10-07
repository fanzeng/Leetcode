class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return int(''.join([str(1 - int(char)) for char in '{:b}'.format(N)]), 2)

test = Solution()
print test.bitwiseComplement(5) # 2
print test.bitwiseComplement(7) # 0
print test.bitwiseComplement(10) # 5
