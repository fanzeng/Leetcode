class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        d = {}
        for r in roads:
            if d.get(r[0]) is None:
                d[r[0]] = 1
            else:
                d[r[0]] += 1
            if d.get(r[1]) is None:
                d[r[1]] = 1
            else:
                d[r[1]] += 1
        importance = 0
        for count in sorted(d.values(), key=lambda x: -x):
            importance += count*n
            n -= 1
        return importance
