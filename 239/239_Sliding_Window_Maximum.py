class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k >= len(nums):
            return [max(nums)]
        res = [None]*(len(nums)-k+1)
        self.heap = MaxHeap(len(nums))
        for i in xrange(k):
            self.heap.insert((nums[i], i))
        res[0] = self.heap.val[0][0]
        for i, num in enumerate(nums[k:]):
            n = i + k
            self.heap.insert((num, i+k))
            while True:
                root = self.heap.val[0]
                if n - root[1]+1 <= k:
                    res[i+1] = root[0]
                    break
                self.heap.pop()
        return res

class Heap(object):
    def __init__(self, isGreater, sz=1):
        self.val = [None]*sz
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
        self.val[self.size - 1] = val
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
    def __init__(self, sz=1):
        isGreater = lambda a, b: a[0] < b[0]
        super(MaxHeap, self).__init__(isGreater, sz)


test = Solution()
print test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) # [3,3,5,5,6,7]
print test.maxSlidingWindow([9,11], 2) # [11]
print test.maxSlidingWindow([4,-2], 2) # [4]
print test.maxSlidingWindow([7,2,4], 2) # [7,4]
print test.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5) # [10,10,9,2]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10], 3) # [10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10], 3) # [10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10]
print test.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4) # [7,7,7,7,7]