class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diff = []
        for person in costs:
            diff.append(person[0] - person[1])
        sorted_costs = [c[0] for c in sorted(zip(costs, diff), key=lambda x: x[1])]
        # print sorted_costs
        res = 0
        for i in xrange(len(costs)/2):
            res += sorted_costs[i][0]
        for i in xrange(len(costs)/2, len(costs)):
            res += sorted_costs[i][1]
        return res

test = Solution()
print test.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) # 110