class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        d = {}
        b = 1
        k = 1
        while b*2 <= m:
            b *= 2
            k += 1
        # print 'k =', k, 'b =', b
        for i in xrange(k):
            d[i] = True
        bit = k - 1

        has_whole_num = False
        while b*2 < n:
            b *= 2
            bit += 1
            has_whole_num = True
        if has_whole_num:
            # print 'the last', bit, 'bits are zero.'
            for j in xrange(k-1, max(-1,k-1-bit), -1):
                # print 'd[', j, '] is set to False'
                d[j] = False

        for i in xrange(m, n+1):
            l = self.toListBinary(i)
            positive = [x for x in xrange(k) if d[x]]
            if len(positive) == 0:
                return 0
            for j in positive:
                # print 'j =', j, 'l =', l
                if j < k-len(l) or l[len(l) - (k-j)] == 0:
                    d[j] = False


        b = 1
        res = 0
        # print 'd =', d
        for i in xrange(k-1, -1, -1):
            if d[i]:
                res += b
            b *= 2
        return res

    def toListBinary(self, n):
        l = []
        b = 1
        k = 1
        while b*2 <= n:
            b *= 2
            k += 1
        while b >= 1:
            l.append(n/b)
            n -= b*l[-1]
            b /= 2
        return l


test = Solution()
print test.rangeBitwiseAnd(5,7) # 4
print test.rangeBitwiseAnd(5,9) # 0
print test.rangeBitwiseAnd(0,1) # 0
print test.rangeBitwiseAnd(1,2) # 0
print test.rangeBitwiseAnd(1,3) # 0
print test.rangeBitwiseAnd(2,2) # 2
print test.rangeBitwiseAnd(16,16) # 16
print test.rangeBitwiseAnd(0,2147483647) # 0
print test.rangeBitwiseAnd(400000,2147483646) # 0
print test.rangeBitwiseAnd(4000000,2147483646) # 0