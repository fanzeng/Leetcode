class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        strength = []
        for i, row in enumerate(mat):
            sum = 0
            for num in row:
                if num == 0:
                    break
                sum += 1
            strength.append([sum, i])
        return [res[1] for res in sorted(strength, key=lambda x:(x[0], x[1]))[:k]]