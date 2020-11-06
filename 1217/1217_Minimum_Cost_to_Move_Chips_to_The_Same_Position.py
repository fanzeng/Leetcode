class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        sum_odd = 0
        sum_even = 0
        for coin in position:
            if coin % 2 == 0:
                sum_even += 1
            else:
                sum_odd += 1
        return min(sum_odd, sum_even)

test = Solution()
print test.minCostToMoveChips([1,2,3]) # 1
print test.minCostToMoveChips([2,2,2,3,3]) # 2
print test.minCostToMoveChips([1,1000000000]) # 1