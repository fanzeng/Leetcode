class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_symbol = self.getListSymbols(s.replace(' ', ''))
        # print 'l_symbol =', l_symbol
        return self.eval(l_symbol)

    def eval(self, l_symbol):
        if len(l_symbol) == 0:
            return 0
        count_mul = l_symbol.count('*')
        count_div = l_symbol.count('/')
        while count_mul + count_div > 0:
            i = l_symbol.index('*') if count_mul > 0 else len(l_symbol)
            j = l_symbol.index('/') if count_div > 0 else len(l_symbol)
            if i < j:
                l_symbol = l_symbol[:i-1] + [l_symbol[i-1]*l_symbol[i+1]] + l_symbol[i+2:]
                count_mul -= 1
            else:
                l_symbol = l_symbol[:j-1] + [l_symbol[j-1]/l_symbol[j+1]] + l_symbol[j+2:]
                count_div -= 1
        res = l_symbol[0]
        i = 1
        while i+1 < len(l_symbol):
            if l_symbol[i] == '+':
                res += l_symbol[i+1]
            else:
                res -= l_symbol[i+1]
            i += 2
        return res

    def getListSymbols(self, s):
        l = []
        i = 0
        str_num = ''
        while i < len(s):
            if s[i] >= '0' and s[i] <= '9':
                str_num += s[i]
            else:
                if len(str_num) > 0:
                    l.append(int(str_num))
                    str_num = ''
                l.append(s[i])
            i += 1
        if len(str_num) > 0:
            l.append(int(str_num))
        return l

test = Solution()
print test.calculate("3+2*2") # 7
print test.calculate(" 3/2 ") # 1
print test.calculate(" 3+5 / 2 ") # 5
print test.calculate("0-2147483647") # -2147483647
print test.calculate("1-1+1") # 1