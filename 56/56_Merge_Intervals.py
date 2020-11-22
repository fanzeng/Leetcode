class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals is None or len(intervals) == 0:
            return intervals
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        start, end = intervals[0]
        for interval in intervals:
            if interval[0] > end:
                res.append([start, end])
                start, end = interval
            else:
                end = max(end, interval[1])
        if not (len(res) > 0 and res[-1][1] == end):
            res.append([start, end])
        return res

test = Solution()
print test.merge([[1,3],[2,6],[8,10],[15,18]]) # [[1,6],[8,10],[15,18]]
print test.merge([[1,4],[4,5]]) # [[1,5]]
print test.merge([[1,4],[2,3]]) # [[1,4]]