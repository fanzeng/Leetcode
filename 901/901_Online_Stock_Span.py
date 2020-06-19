class StockSpanner(object):

    def __init__(self):
        self.arr = []
        self.res = []
        self.size = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.arr.append(price)
        self.size += 1
        res = 1
        if len(self.res) == 0: # first time
            self.res.append(res)
            return res
        i = self.size-2
        while price >= self.arr[i] and i >= 0:
            step = self.res[i]
            res += step
            i -= step
        self.res.append(res)
        return res


prices = []
prices.append([100, 80, 60, 70, 60, 75, 85]) # [1, 1, 1, 2, 1, 4, 6]
prices.append([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
prices.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in xrange(len(prices)):
    print 'price =', prices[i]
    obj = StockSpanner()
    for price in prices[i]:
        print obj.next(price)



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)