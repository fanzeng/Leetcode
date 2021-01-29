class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        return self.validSquareDiag(p1, p2, p3, p4) or self.validSquareDiag(p1, p3, p2, p4) or self.validSquareDiag(p1, p4, p2, p3)

    def validSquareDiag(self, a, c, b, d):
        diag0 = Vector(a[0]-c[0], a[1]-c[1])
        diag1 = Vector(b[0]-d[0], b[1]-d[1])
        mid_2_0 = Vector(a[0] + c[0], a[1] + c[1])
        mid_2_1 = Vector(b[0] + d[0], b[1] + d[1])
        return diag0.len_sq > 0 and diag0.len_sq == diag1.len_sq and mid_2_0 == mid_2_1 and diag0.isPerpendicularTo(diag1)

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.len_sq = x*x + y*y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def isPerpendicularTo(self, other):
        return self.dot(other) == 0

test = Solution()
print test.validSquare([0,0], [1,1], [1,0], [0,1])