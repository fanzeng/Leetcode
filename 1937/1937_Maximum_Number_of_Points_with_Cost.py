class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points is None or len(points) == 0:
            return 0
        m = len(points)
        n = len(points[0])
        scores = [points[-1]]
        for i in range(m-2, -1, -1):
            row = points[i]
            left = self.getScore(row, scores[-1])
            right = self.getScore(row[::-1], scores[-1][::-1])[::-1]
            scores.append([max(l, r) for (l, r) in zip(left, right)])
        return max(scores[-1])

    def getScore(self, row, prev):
        n = len(prev)
        score = [0] * n
        j = 0
        k = 0
        q = prev[k]
        while j < n:
            p = row[j]
            if prev[j] > q - (j-k):
                q = prev[j]
                k = j
            score[j] = p + q - abs(j-k) 
            j += 1
        return score

    # 1014_Best_Sightseeing_Pair, for reference
    def maxScorePair(self, values):
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
