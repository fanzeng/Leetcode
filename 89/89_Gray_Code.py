class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        gray_code_binary = self.grayCodeBinary(n)
        return [int(code, 2) for code in gray_code_binary]

    def grayCodeBinary(self, n):
        if n == 1:
            return ['0', '1']
        prev = self.grayCodeBinary(n-1)
        return ['0' + b for b in prev] + ['1' + b for b in prev[::-1]]

test = Solution()
print test.grayCode(1) # [0,1]
print test.grayCode(2) # [0,1,3,2]
print test.grayCode(3) # [0,1,3,2,6,7,5,4]
print test.grayCode(4)