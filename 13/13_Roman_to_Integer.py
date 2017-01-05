class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        list_s = list(s)
        while(list_s):
            if len(list_s) == 1:
                res += d[list_s.pop()]
            elif d[list_s[-1]] <= d[list_s[-2]]:
                res += d[list_s.pop()]
            else:
                res += d[list_s.pop()] - d[list_s.pop()]
        return res


def main():
    test = Solution()
    print test.romanToInt('II')
    print test.romanToInt('IV')
    print test.romanToInt('XIV')
    print test.romanToInt('CD')
    print test.romanToInt('MCDVIII')


main()