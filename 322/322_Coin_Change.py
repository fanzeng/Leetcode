class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coins = sorted(coins, reverse=True)
        self.d = {}
        return self.coinChangeDP(amount)

    def coinChangeDP(self, amount):
        if self.d.get(amount) is not None:
            return self.d.get(amount)
        if amount <= 0:
            return 0
        l_res = [self.coinChangeDP(amount - coin) for coin in self.coins if amount - coin >= 0]
        l_res = [x for x in l_res if x != -1]
        if len(l_res) > 0:
            res = 1 + min(l_res)
        else:
            res = -1
        self.d[amount] = res
        return res

test = Solution()
print test.coinChange([1,2,5], 11) # 3
print test.coinChange([2], 3) # -1
print test.coinChange([1], 2) # 2