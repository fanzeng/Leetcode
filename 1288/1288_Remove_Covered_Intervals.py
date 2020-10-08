class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sorted_intervals = sorted(intervals, key=lambda x:(x[0], -x[1]))
        res = [sorted_intervals[0]]
        end = sorted_intervals[0][1]
        for intv in sorted_intervals:
            if intv[1] <= end:
                continue
            res.append(intv)
            end = intv[1]
        return len(res)

test = Solution()
print test.removeCoveredIntervals([[1,4],[3,6],[2,8]]) # 2
print test.removeCoveredIntervals([[1,4],[2,3]]) # 1
print test.removeCoveredIntervals([[0,10],[5,12]]) # 2
print test.removeCoveredIntervals([[3,10],[4,10],[5,11]]) # 2
print test.removeCoveredIntervals([[1,2],[1,4],[3,4]]) # 1