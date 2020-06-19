class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        if len(citations) == 1:
            return int(citations[0] >= 1)
        l = 0
        r = len(citations)-1

        while l < r-1:
            m = (l + r)/2
            if (len(citations)-m) < citations[m]:
                r = m
            elif (len(citations)-m) >= citations[m]:
                l = m
        if citations[l] >= len(citations)-l:
            return len(citations)-l
        else:
            return min(citations[r], len(citations)-r)

test = Solution()
print test.hIndex([0,1,3,5,6]) # 3
print test.hIndex([1,1,1,2,5,6,7,8]) # 4
print test.hIndex([1,1,1,1,1,1,1,1,2]) # 1
print test.hIndex([1,1,7,7,7,7,7,7,7]) # 7
print test.hIndex([10]) # 1
print test.hIndex([0,1]) # 1
print test.hIndex([0,0,4,4]) # 2
print test.hIndex([0]) # 0
print test.hIndex([0,0]) # 0

