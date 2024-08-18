class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        s = values[0] + values[1] - 1
        l = len(values)
        while j < l:
            d = j - i
            s = max(s, values[i] + values[j] - d)
            if values[i] - d < values[j]:
                i = j
            j += 1
        return s
