class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in xrange(len(cost)):
            can_complete = self.canCompleteCircuitSingleStart(self.rotate(gas, i), self.rotate(cost, i))
            if can_complete:
                return i
        return -1

    def canCompleteCircuitSingleStart(self, gas, cost):
        # print gas, cost
        tank = 0
        for i in xrange(len(cost)):
            tank += gas[i] - cost[i]
            if tank < 0:
                return False
        return True

    def rotate(self, arr, i):
        return arr[i:] + arr[:i]


test = Solution()
print test.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) # 3
print test.canCompleteCircuit([2,3,4], [3,4,3]) # -1
print test.canCompleteCircuit([5,8,2,8], [6,5,6,6]) # 3




