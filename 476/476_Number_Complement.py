class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = self.toBinary(num)
        if s[0] == '0' and len(s) > 1:
             s = s[1:]
        compl = ''.join([str(1-int(x)) for x in list(s)])
        return self.fromBinary(compl)

    def toBinary(self, num):
        if num == 0:
            return '0'
        if num == 1:
            return '1'
        b = 1
        while b <= num:
            b *= 2
        s = ''
        while b > 1:
            b /= 2
            bit = num/b
            s += str(bit)
            num -= bit*b
        return s

    def fromBinary(self, s):
        num = 0
        b = 1
        for i in xrange(len(s)-1, -1, -1):
            num += int(s[i])*b
            b *= 2
        return num

test = Solution()
print test.findComplement(0)
print test.findComplement(1)
print test.findComplement(2)
print test.findComplement(5)
print test.findComplement(9)