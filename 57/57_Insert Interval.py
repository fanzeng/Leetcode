class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        self.intervals = intervals
        unprocessed = self.intervals[:]
        res = []
        merged_interval = newInterval
        for interval in unprocessed:
            if self.isOverlap(merged_interval, interval):
                # print 'merging', interval, merged_interval
                merged_interval = self.mergeInterval(interval, merged_interval)
            else:
                res.append(interval)
        res.append(merged_interval)
        return sorted(res, key=lambda x:x[0])


    def isOverlap(self, a, b):
        return a[1] >= b[0] and b[1] >= a[0]

    def mergeInterval(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]

test = Solution()
print test.insert([[1,3],[6,9]], [2,5]) # [[1,5],[6,9]]
print test.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) # [[1,2],[3,10],[12,16]]