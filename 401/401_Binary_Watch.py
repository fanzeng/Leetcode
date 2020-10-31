class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in xrange(min(5, num+1)):
            l_h = self.getListNum(12, i)
            l_m = self.getListNum(60, num-i)
            for h in l_h:
                for m in l_m:
                    res.append(self.toStr(h, m))
        return res

    def getListNum(self, max_num, i):
        li = []
        for x in xrange(max_num):
            if '{:b}'.format(x).count('1') == i:
                li.append(x)
        return li

    def toStr(self, h, m):
        return str(h) + ':' + '{:02d}'.format(m)

test = Solution()
print test.readBinaryWatch(1) # ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]