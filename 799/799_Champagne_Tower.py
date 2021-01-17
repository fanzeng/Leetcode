class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        self.res_champagne_level = []
        next_champagne_level = [poured]
        for row in xrange(query_row+1):
            champagne_level, next_champagne_level = self.pour(next_champagne_level)
            self.res_champagne_level.append(champagne_level)
        # print self.res_champagne_level
        return self.res_champagne_level[query_row][query_glass]

    def pour(self, champagne_level):
        next_champagne_level = [0.]*(len(champagne_level)+1)
        for i, glass in enumerate(champagne_level):
            if glass > 1.0:
                champagne_level[i] = 1.0
                spill_over = glass - 1.0
                next_champagne_level[i] += spill_over / 2.0
                next_champagne_level[i+1] += spill_over / 2.0
        # print champagne_level, next_champagne_level
        return champagne_level, next_champagne_level

test = Solution()
print test.champagneTower(1,1,1) # 0
print test.champagneTower(2,1,1) # 0.5
