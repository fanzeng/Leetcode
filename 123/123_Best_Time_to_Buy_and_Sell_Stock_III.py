class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0
        diff = []
        for i in xrange(len(prices)-1):
            diff.append(prices[i+1]-prices[i])
        # print 'diff=', diff
        max_profit = max(0, self.maxSubArray(diff))
        for i in xrange(1, len(diff)-1):
            if diff[i]*diff[i-1] < 0:
                max_sub_array_front = self.maxSubArray(diff[:i])
                max_sub_array_back = self.maxSubArray(diff[i:])
                max_profit = max(max_profit, max_sub_array_front + max_sub_array_back)
            # print max_sub_array_back, max_sub_array_front, max_profit
        return max_profit

    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            sum_since_reset = nums[0]
            max_sum = sum_since_reset
            for i in range(1, len(nums)):
                sum_since_reset += nums[i]
                if nums[i] > sum_since_reset:
                    sum_since_reset = nums[i]
                max_sum = max(max_sum, sum_since_reset)
            return max_sum

    # def maxSubArrayBound(self, nums):
    #     if len(nums) == 1:
    #         return nums[0], 0, 0
    #     else:
    #         sum_since_reset = nums[0]
    #         max_sum = sum_since_reset
    #         start = 0
    #         end = 0
    #         max_start = start
    #         max_end = end
    #         for i in range(1, len(nums)):
    #             sum_since_reset += nums[i]
    #             end = i
    #             if nums[i] > sum_since_reset:
    #                 sum_since_reset = nums[i]
    #                 start = i
    #                 end = i
    #             if sum_since_reset > max_sum:
    #                 max_sum = sum_since_reset
    #                 max_start = start
    #                 max_end = end
    #             max_sum = max(max_sum, sum_since_reset)
    #         return max_sum, max_start, max_end

test = Solution()
print test.maxProfit([3,3,5,0,0,3,1,4])
print test.maxProfit([1,2,3,4,5])
print test.maxProfit([7,6,4,3,1])
print test.maxProfit([1,2,4,2,5,7,2,4,9,0])




# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.