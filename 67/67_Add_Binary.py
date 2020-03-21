class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bitCount = 0
        carry = '0'
        sum = ''
        while bitCount < max(len(a), len(b)):
            bitCount += 1
            if bitCount <= len(a):
                bita = a[-bitCount]
            else:
                bita = '0'
            if bitCount <= len(b):
                bitb = b[-bitCount]
            else:
                bitb = '0'
            result, carry = self.addBitWithCarry(bita, bitb, carry)
            sum = result + sum
        if carry == '1':
            sum = '1' + sum
        return sum
    # add two chars of either '1' or '0', returns (result, carry)
    def addBitWithCarry(self, a, b, carry):
        if carry == '0':
            if a == '0' and b == '0':
                return '0', '0'
            elif a == '1' and b == '1':
                return '0', '1'
            else:
                return '1', '0'
        else:
            if a != b:
                return '0', '1'
            else:
                return '1', a

test = Solution()
print test.addBinary("11", "1")
print test.addBinary("1010", "1011")
print test.addBinary("0", "0")
print test.addBinary("1", "1")
print test.addBinary("1", "0")
print test.addBinary("11111111", "11111111")


# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"