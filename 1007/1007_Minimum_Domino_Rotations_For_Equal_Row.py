class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        d = {}
        for j, num in enumerate(A):
            if d.get(num) is None:
                d[num] = {j}
            else:
                d[num].add(j)
        for k, num in enumerate(B):
            if d.get(num) is None:
                d[num] = {k}
            else:
                d[num].add(k)
        min_rot = len(A)           
        for i in range(1,7):
            if d.get(i) is not None and len(d.get(i)) == len(A):
                rot = self.getRot(A, B, i)
                if rot < min_rot:
                    min_rot = rot
        if min_rot < len(A):
            return min_rot
        else:
            return -1

    def getRot(self, A, B, i):
        count_A = 0
        for num in A:
            if num != i:
                count_A += 1
        count_B = 0
        for num in B:
            if num != i:
                count_B += 1
        return min(count_A, count_B)

test = Solution()
print test.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]) # 2
print test.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]) # -1
print test.minDominoRotations([1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]) # 0
