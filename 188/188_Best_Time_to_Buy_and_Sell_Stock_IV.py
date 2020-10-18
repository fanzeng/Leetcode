class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        diff = [prices[i] - prices[i-1] for i in xrange(1, len(prices))]
        # print diff
        l_merged, l_pos = self.merge(diff)
        # print l_merged, l_pos
        # if k allows us to pick all positives, simply do so and return
        if len(l_pos) <= k:
            return sum(l_pos)
        # we are not allowed to pick all positives, so we will need to compromise
        for count in xrange(len(l_pos)-k):
            l_merged = self.mergePos(l_merged)
            # print 'count, l_merged =', count, l_merged
        return sum([n for n in l_merged if n > 0])

    def merge(self, arr):
        l_pos = []
        l_merged = []
        sum_pos = 0
        sum_neg = 0
        arr = [n for n in arr if n != 0] # ignore zeros
        for i, num in enumerate(arr):
            if num < 0:
                if sum_pos > 0:
                    l_pos.append(sum_pos)
                    l_merged.append(sum_pos)
                    sum_pos = 0
                sum_neg += num
                continue
            # num is positive
            # if this is the first positive
            if sum_neg < 0 and len(l_merged) > 0:
                l_merged.append(sum_neg)
            sum_neg = 0
            sum_pos += num
            if i == len(arr)-1:
                l_merged.append(sum_pos)
                l_pos.append(sum_pos)
        return l_merged, l_pos

    # merge adjacent positives if profitable
    # assumes arr is alternating between pos and neg, and starting and ending with pos
    def mergePos(self, arr):
        min_pos_loc = min([(i, arr[i]) for i in xrange(len(arr)) if arr[i] > 0], key=lambda x:x[1])[0]
        max_neg_loc = max([(i, arr[i]) for i in xrange(len(arr)) if arr[i] < 0], key=lambda x:x[1])[0]
        # print 'min_pos_loc, max_neg_loc =', min_pos_loc, max_neg_loc
        if arr[min_pos_loc] <= -arr[max_neg_loc]: # if amount lost by removing min pos is smaller, remove min pos
            new_neg = sum(arr[min_pos_loc-1:min_pos_loc+2])
            l_new_neg = [new_neg] if new_neg < 0 and min_pos_loc + 2 < len(arr) else []
            return arr[:max(0, min_pos_loc-1)] + l_new_neg + arr[min_pos_loc+2:]
        else:
            new_pos = sum(arr[max_neg_loc-1:max_neg_loc+2])
            return arr[:max_neg_loc-1] + [new_pos] + arr[max_neg_loc+2:]

test = Solution()
print test.maxProfit(2, [2,4,1]) # 2
print test.maxProfit(2, [3,2,6,5,0,3]) # 7
print test.maxProfit(2, [3,2,6,5,0,3,2,3]) # 7
print test.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]) # 13
print test.maxProfit(2, [2,6,8,7,8,7,9,4,1,2,4,5,8]) # 14
print test.maxProfit(2, [3,3,5,0,0,3,1,4]) # 6
print test.maxProfit(2, [5,2,3,2,6,6,2,9,1,0,7,4,5,0]) # 14
print test.maxProfit(2, [0,5,5,6,2,1,1,3]) # 8
print test.maxProfit(2, [1,9,6,9,1,7,1,1,5,9,9,9]) # 16