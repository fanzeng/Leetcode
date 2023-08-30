class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        p = purchaseAmount
        a = purchaseAmount / 10 * 10
        b = (purchaseAmount / 10 + 1)*10
        if p - a == b - p:
            return 100 - b
        elif p - a < b - p:
            return 100 - a
        else:
            return 100 - b
