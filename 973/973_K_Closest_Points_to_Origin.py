class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        self.minHeap = MinHeap()
        is_greater = lambda a, b: self.getDistanceSquare(a) > self.getDistanceSquare(b)
        for point in points:
            self.minHeap.insert(point, is_greater)
        res = []
        for i in xrange(K):
            res.append(self.minHeap.pop(is_greater))
        return res

    def getDistanceSquare(self, point):
        return point[0]*point[0] + point[1]*point[1]


class MinHeap(object):
    def __init__(self):
        self.val = []
        self.size = 0

    def parent(self, i):
        return (i-1)/2

    def child(self, i):
        return 2*i + 1, 2*i + 2

    def swap(self, i, j):
        temp = self.val[i]
        self.val[i] = self.val[j]
        self.val[j] = temp

    def float(self, i, isGreater):
        if i > 0:
            parent_id = self.parent(i)
            if isGreater(self.val[parent_id], self.val[i]):
                self.swap(parent_id, i)
                i = self.float(parent_id, isGreater)
        return i

    def insert(self, val, isGreater):
        self.val.append(val)
        self.size += 1
        i = self.float(self.size-1, isGreater)
        return i

    def sink(self, i, isGreater):
        children_id = self.child(i)
        if children_id[0] >= self.size:
            return i
        if children_id[1] >= self.size:
            smaller_child_id = children_id[0]
        elif isGreater(self.val[children_id[0]], self.val[children_id[1]]):
            smaller_child_id = children_id[1]
        else:
            smaller_child_id = children_id[0]
        if isGreater(self.val[i], self.val[smaller_child_id]):
            self.swap(smaller_child_id, i)
            i = self.sink(smaller_child_id, isGreater)
        return i

    def pop(self, isGreater):
        if len(self.val) == 0:
            return None
        root = self.val[0]
        self.swap(0, self.size-1)
        self.size -= 1
        i = self.sink(0, isGreater)
        return root

test = Solution()
print test.kClosest([[1,3],[-2,2]], 1) # [[-2,2]]
print test.kClosest([[3,3],[5,-1],[-2,4]], 2) # [[3,3],[-2,4]]
print test.kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3) # [[0,2],[-3,3],[-2,5]]