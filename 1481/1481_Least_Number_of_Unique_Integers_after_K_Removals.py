class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        for n in arr:
            if d.get(n) is None:
                d[n] = 1
            else:
                d[n] += 1
        counts = sorted(d.values())
        removed = 0
        i = 0
        while i < len(counts):
            if removed + counts[i] > k:
                break
            removed += counts[i]
            i += 1
        return len(counts) - i
