class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        remain = len(num) - k
        if remain == 0:
            return '0'
        res = self.selectDigits(num, remain)
        if int(res) > 0:
            return res.lstrip('0')
        else:
            return '0'

    def selectDigits(self, num, n):
        if n == 1:
            candidate = [int(x) for x in num]
            return str(min(candidate))
        candidate = [int(x) for x in num[:-n+1]]

        select = 10
        loc = 0
        for i, c in enumerate(candidate):
            if c < select:
                select = c
                loc = i
        # print candidate, loc, select
        res = str(select) + self.selectDigits(num[loc+1:], n-1)
        return res

test = Solution()
print test.removeKdigits("1432219", 3) # 1219
print test.removeKdigits("10200", 1) # 200
print test.removeKdigits("10", 2) # 0
print test.removeKdigits("10", 1) # 0