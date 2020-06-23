class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            while not self.hasIntersect(A[i], B[j]):
                if A[i][1] < B[j][0]:
                    i += 1
                elif B[j][1] < A[i][0]:
                    j += 1
                if i >= len(A) or j >= len(B):
                    return res

            res.append(self.getIntersect(A[i], B[j]))
            if A[i][1] < B[j][1]:
                i += 1
            elif B[j][1] < A[i][1]:
                j += 1
            else:
                i += 1
                j += 1
        return res

    def hasIntersect(self, a, b):
        if a[1] >= b[0] and a[1] <= b[1]:
            return True
        if b[1] >= a[0] and b[1] <= a[1]:
            return True
        return False

    def getIntersect(self, a, b):
        return [max(a[0], b[0]), min(a[1], b[1])]

test = Solution()
print test.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])
print test.intervalIntersection([[1,8],[16,20]], [[2,11],[12,13]])