class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if coins is None or len(coins) == 0:
            return int(amount == 0)
        self.d = {}
        self.coins = sorted(coins)[::-1]
        self.max_coin = self.coins[0]
        return self.changeDP(amount, self.coins)

    def changeDP(self, amount, coins):
        d_res = self.d.get(self.getHash(amount, coins))
        if d_res is not None:
            return d_res
        # coins = sorted(coins)[::-1] # This is not necessary if it's done in the caller.
        if len(coins) == 1:
            res = int(amount % coins[-1] == 0)
        else:
            res = 0
            coin = coins[0]
            count = 0
            while amount > coin*count:
                res += self.changeDP(amount - coin*count, coins[1:])
                count += 1
            if amount == coin*count:
                res += 1
        # print 'amount =', amount, 'coins =', coins, 'res =', res
        self.d[self.getHash(amount, coins)] = res
        return res

    def getHash(self, amount, coins):
        return (amount, tuple(coins))

test = Solution()
print test.change(5, [1,2,5]) # 4
print test.change(3, [2]) # 0
print test.change(10, [10]) # 1