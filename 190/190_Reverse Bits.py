class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1], 2)


test = Solution()
print test.reverseBits(43261596) # 964176192
