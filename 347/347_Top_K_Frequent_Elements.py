class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        self.d = {}
        for n in nums:
            if self.d.get(n) is None:
                self.d[n] = 1
            else:
                self.d[n] += 1

        self.max_pq = MaxHeap(self.d)
        for n in self.d.keys():
            self.max_pq.insert(n)
        res = []
        for i in xrange(k):
            res.append(self.max_pq.pop())
        return res

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
        self.val.append(val)
        self.size += 1
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


class MaxHeap(Heap):
    def __init__(self, d):
        isGreater = lambda a, b: d[a] < d[b]
        super(MaxHeap, self).__init__(isGreater)

test = Solution()
print test.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print test.topKFrequent([1], 1) # [1]