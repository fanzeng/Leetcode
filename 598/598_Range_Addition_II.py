class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops is None or len(ops) == 0:
            return m*n
        min_h = m
        min_w = n
        for op in ops:
            h, w = op
            if h < min_h:
                min_h = h
            if w < min_w:
                min_w = w
        return min_h*min_w

test = Solution()
print test.maxCount(3, 3, [[2,2],[3,3]]) # 4
print test.maxCount(3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]) # 4
print test.maxCount(3, 3, []) # 9
print test.maxCount(92, 2, [[70,1],[37,1],[3,2],[67,1],[37,2],[87,2],[26,1],[43,1],[19,1],[63,1],[67,1],[19,1],[14,2],[5,1],[27,2],[44,2],[13,1]]) # 3