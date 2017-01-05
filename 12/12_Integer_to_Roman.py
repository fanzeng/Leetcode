class Solution(object):
    d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        #  Input is guaranteed to be within the range from 1 to 3999.
        # Note: 4 and 9 must be treated specially


        remain = num
        Roman = ''
        level =1000
        while level >= 1:
            remain, partRoman = self.getRoman(remain, level)
            Roman += partRoman
            level /= 10
        return Roman

    def getRoman(self, remain, level):
        res = ''
        while(remain >= level):
            if remain > level*5:
                remain -= level*5
                res += self.d[level*5]
            else:
                remain -= level
                res += self.d[level]
        return remain, res

def main():
    test = Solution()
    # print test.intToRoman(2)
    # print test.intToRoman(4)
    # print test.intToRoman(14)
    # print test.intToRoman(400)
    print test.intToRoman(1408)
    print test.intToRoman(2517)


main()