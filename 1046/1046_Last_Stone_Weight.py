class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 0:
            return None
        elif len(stones) == 1:
            return stones[0]
        stones.sort(reverse=True)
        while len(stones) > 1:
            stones = self.smash(stones)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0

    def smash(self, stones):
        a = stones.pop(0)
        b = stones.pop(0)
        if a == b:
            return stones
        else:
            c = abs(a-b)
            if len(stones) == 0:
                return [c]
            i = len(stones)-1
            while stones[i] < c and i >= 0:
                i -= 1
            stones.insert(i+1, c)
            return stones

test = Solution()
print test.lastStoneWeight([2, 7, 4, 1, 8, 1])
print test.lastStoneWeight([2, 2])
print test.lastStoneWeight([7,6,7,6,9])
print test.lastStoneWeight([9,10,4,5,7,1])
# Note:
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
# Accepted