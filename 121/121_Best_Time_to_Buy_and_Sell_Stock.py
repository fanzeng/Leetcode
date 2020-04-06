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
        max_sub_array = self.maxSubArray(diff)
        if max_sub_array > 0:
            return max_sub_array
        else:
            return 0

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

test = Solution()
print test.maxProfit([7,1,5,3,6,4])
print test.maxProfit([7,6,4,3,1])
print test.maxProfit([7])
print test.maxProfit([])


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.