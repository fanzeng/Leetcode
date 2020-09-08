class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        self.days = days
        self.lendays = len(self.days)
        self.costs = costs
        self.cost1 = costs[0]
        self.cost7 = costs[1]
        self.cost30 = costs[2]

        self.d = {}
        self.mincostTicketsDP()
        return self.d[self.days[0]]

    def mincostTicketsDP(self):
        self.d[self.days[-1]] = min(self.costs)

        for i in xrange(len(self.days)-2, -1, -1):
            day = self.days[i]
            day_after_7 = self.getDayAfter(i, 7)
            day_after_30 = self.getDayAfter(i, 30)

            cost_buy1 = self.cost1 + self.d[self.days[i + 1]]
            cost_buy7 = self.cost7
            if day_after_7 is not None:
                cost_buy7 += self.d[day_after_7]
            cost_buy30 = self.cost30
            if day_after_30 is not None:
                cost_buy30 += self.d[day_after_30]

            self.d[day] = min([cost_buy1, cost_buy7, cost_buy30])

    # returns first day not covered by buying a ticket of "period" on day_id
    def getDayAfter(self, day_id, period):
        today = self.days[day_id]
        for day in self.days[day_id:]:
            if day > today + period - 1:
                return day

test = Solution()
print test.mincostTickets([1,4,6,7,8,20], [2,7,15]) # 11
print test.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) # 17
print test.mincostTickets([1,4,6,7,8,20], [7,2,15]) # 6