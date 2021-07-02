class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = MinHeap()
        for num in arr:
            heap.insert((num, abs(x-num)))
        res = []
        for i in xrange(k):
            res.append(heap.pop()[0])
        return sorted(res)

class Heap(object):
    def __init__(self, isGreater):
        self.val = []
        self.size = 0
        self.isGreater = isGreater

    def parent(self, i):
        return (i-1)/2

    def child(self, i):
        return 2*i + 1, 2*i + 2

    def swap(self, i, j):
        temp = self.val[i]
        self.val[i] = self.val[j]
        self.val[j] = temp

    def float(self, i):
        if i > 0:
            parent_id = self.parent(i)
            if self.isGreater(self.val[parent_id], self.val[i]):
                self.swap(parent_id, i)
                i = self.float(parent_id)
        return i

    def insert(self, val):
        self.size += 1
        if len(self.val) >= self.size:
            self.val[self.size-1] = val
        else:
            self.val.append(val)
        i = self.float(self.size-1)
        return i

    def sink(self, i):
        children_id = self.child(i)
        if children_id[0] >= self.size:
            return i
        if children_id[1] >= self.size:
            smaller_child_id = children_id[0]
        elif self.isGreater(self.val[children_id[0]], self.val[children_id[1]]):
            smaller_child_id = children_id[1]
        else:
            smaller_child_id = children_id[0]
        if self.isGreater(self.val[i], self.val[smaller_child_id]):
            self.swap(smaller_child_id, i)
            i = self.sink(smaller_child_id)
        return i

    def pop(self):
        if len(self.val) == 0:
            return None
        root = self.val[0]
        self.swap(0, self.size-1)
        self.size -= 1
        i = self.sink(0)
        return root

class MinHeap(Heap):
    def __init__(self):
        isGreater = lambda a, b: a[1] > b[1] if a[1] != b[1] else a[0] > b[0]
        super(MinHeap, self).__init__(isGreater)

test = Solution()
print test.findClosestElements([1,2,3,4,5], 4, 3) # [1,2,3,4]
print test.findClosestElements([1,2,3,4,5], 4, -1) # [1,2,3,4]
print test.findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5) # [3,3,4]