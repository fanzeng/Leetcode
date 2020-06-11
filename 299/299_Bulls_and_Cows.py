class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        list_bull = []
        d = {}
        for i, c in enumerate(guess):
            if secret[i] == c:
                bull += 1
                list_bull.append(i)
            else:
                if d.get(secret[i]) is None:
                    d[secret[i]] = [i]
                else:
                    d[secret[i]].append(i)
        for i, c in enumerate(guess):
            if i in list_bull or d.get(c) is None:
                continue
            cow += 1
            if len(d.get(c)) == 1:
                d.pop(c)
            else:
                d[c] = d.get(c)[1:]
        return str(bull) + 'A' + str(cow) + 'B'

test = Solution()
print test.getHint("1807", "7810") # 1A3B
print test.getHint("1123", "0111") # 1A1B
print test.getHint("11", "10") # 1A0B
print test.getHint("1807", "7810") # 1A3B