class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            num = -num
            is_neg = True
        else:
            is_neg = False
        p = 2**32
        l_bit = []
        while p > 1:
            bit = num / p
            l_bit.append(bit)
            num -= bit*p
            p /= 16
        l_bit.append(num)
        if is_neg:
            l_bit = [15-b for b in l_bit]
            l_bit[-1] += 1
            for i in xrange(len(l_bit)-1, -1, -1):
                if l_bit[i] == 16:
                    l_bit[i] = 0
                    if i > 0:
                        l_bit[i-1] += 1
        # print l_bit
        return ''.join([self.bitToStr(b) for b in l_bit[1:]]).lstrip('0')

    def bitToStr(self, b):
        if b < 10:
            return str(b)
        return chr(ord('a') + (b-10))

test = Solution()
print test.toHex(26) # "1a"
print test.toHex(0) # "0"
print test.toHex(16) # "10"
print test.toHex(2**31) # "80000000"
print test.toHex(-1) # "ffffffff"
print test.toHex(-2) # "fffffffe"
print test.toHex(-15) # "fffffff1"
print test.toHex(-16) # "fffffff0"
print test.toHex(-17) # "ffffffef"
print test.toHex(-128) # "ffffff80"