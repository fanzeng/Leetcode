class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        self.A = A
        self.B = B
        self.h = len(A)
        self.w = len(A[0])
        max_overlap = self.calcOverlap(0, 0)
        for absdy in xrange(self.h):
            max_overlap = max([max_overlap, self.calcOverlap(absdy, 0), self.calcOverlap(-absdy, 0)])
            l_overlap = []
            for absdx in xrange(1, self.w):
                if (self.h-absdy)*(self.w-absdx) < max_overlap:
                    continue
                l_overlap.append(self.calcOverlap(absdy, absdx))
                l_overlap.append(self.calcOverlap(absdy, -absdx))
                if absdy > 0:
                    l_overlap.append(self.calcOverlap(-absdy, absdx))
                    l_overlap.append(self.calcOverlap(-absdy, -absdx))
                overlap = max(l_overlap)
                if overlap > max_overlap:
                    max_overlap = overlap
        return max_overlap

    def calcOverlap(self, dy, dx):
        overlap = 0
        for i in xrange(self.h):
            for j in xrange(self.w):
                a = self.A[i][j]
                k = i-dy
                l = j-dx
                if k < 0 or k >= self.h or l < 0 or l >=self.w:
                    continue
                b = self.B[k][l]
                if a == 1 and b == 1:
                    overlap += 1
        return overlap

test = Solution()
print test.largestOverlap(
    [[1,1,0],
     [0,1,0],
     [0,1,0]],
    [[0,0,0],
     [0,1,1],
     [0,0,1]]
) # 3