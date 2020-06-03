class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        b = 1
        s = 0
        while True:
            b *= 26
            s += b
            if s >= n:
                break

        res = ''
        n -= 1
        while b > 1:
            s -= b
            b /= 26
            t = (n-s)/b
            n -= b*(t+1)
            res += chr(ord('A') + t)
        return res

test = Solution()
print test.convertToTitle(1) # 'A'
print test.convertToTitle(28) # 'AB'
print test.convertToTitle(701) # 'ZY'
print test.convertToTitle(26) # 'Z'
print test.convertToTitle(52) # 'AZ'