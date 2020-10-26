class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        self.d = {1: True, 2:False}
        return self.winnerSquareGameDP(n)

    def winnerSquareGameDP(self, n):
        if self.d.get(n) is not None:
            return self.d[n]
        i = 0
        while True:
            i += 1
            isq = i*i
            if isq > n:
                break
            if not self.winnerSquareGameDP(n -isq):
                # print 'f(', n, ') =', True
                self.d[n] = True
                return True
        # print 'f(', n, ') =', False
        self.d[n] = False
        return False

test = Solution()
print test.winnerSquareGame(1) # True
print test.winnerSquareGame(2) # False
print test.winnerSquareGame(4) # True
print test.winnerSquareGame(7) # False
print test.winnerSquareGame(17) # False
print test.winnerSquareGame(99) # True

