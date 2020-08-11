class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        d = {}
        for c in citations:
            if d.get(c) is None:
                d[c] = 1
            else:
                d[c] += 1
        accu_paper_count = 0
        h = 0
        for citation_count, paper_count in sorted(d.items(), key=lambda x:-x[0]):
            # print citation_count, paper_count
            accu_paper_count += paper_count
            h = max(h, min(accu_paper_count, citation_count))
        return h

test = Solution()
print test.hIndex([3,0,6,1,5]) # 3
print test.hIndex([100]) # 1
print test.hIndex([11,15]) # 2
print test.hIndex([4,4,0,0]) # 2