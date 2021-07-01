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
        res[0] = max(nums[:k])
        self.heap = MaxHeap(len(nums), k)
        for num in nums[:k]:
            self.heap.popInsert(num)

        i = 1
        for num in nums[k:]:
            self.heap.popInsert(num)
            res[i] = self.heap.val[0]
            i += 1
        return res

class Heap(object):
    def __init__(self, isGreater, sz=1, k=1):
        self.val = [None]*sz
        self.k = k
        self.recent = []
        self.size = 0
        self.isGreater = isGreater

    def parent(self, i):
        return (i-1)/2

    def child(self, i):
        return 2*i + 1, 2*i + 2

    def swap(self, i, j):
        if i == j:
            return
        i_new = None
        j_new = None
        if i in self.recent:
            i_old_id = self.recent.index(i)
            i_new = j
        if j in self.recent:
            j_old_id = self.recent.index(j)
            j_new = i
        if i_new is not None:
            # print 'self.recent[', i_old_id, '] =', i_new
            self.recent[i_old_id] = i_new
        if j_new is not None:
            # print 'self.recent[', j_old_id, '] =', j_new
            self.recent[j_old_id] = j_new

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

    # dev helper function to verify whether self is still a heap
    def _isHeap(self, i):
        if i >= self.size:
            return False
        children_id = self.child(i)
        if children_id[0] < self.size:
            if self.isGreater(self.val[i], self.val[children_id[0]]):
                return False
            is_first_child_heap = self._isHeap(children_id[0])
        else:
            is_first_child_heap = True
        if children_id[1] < self.size:
            if self.isGreater(self.val[i], self.val[children_id[1]]):
                return False
            is_second_child_heap = self._isHeap(children_id[1])
        else:
            is_second_child_heap = True
        return is_first_child_heap and is_second_child_heap

    def _find(self, val, start):
        if start >= self.size:
            return None
        if self.val[start] == val:
            return start
        children_id = self.child(start)
        if children_id[0] < self.size:
            if self.val[children_id[0]] == val:
                return children_id[0]
            elif self.isGreater(val, self.val[children_id[0]]):
                first = self._find(val, children_id[0])
                if first:
                    return first
        if children_id[1] < self.size:
            if self.val[children_id[1]] == val:
                return children_id[1]
            elif self.isGreater(val, self.val[children_id[1]]):
                return self._find(val, children_id[1])

    def find(self, val):
        return self._find(val, 0)

    def popAt(self, i):
        val = self.val[i]
        if i == self.size-1:
            self.size -= 1
            return val
        self.swap(i, self.size-1)
        self.size -= 1
        v = self.val[i]
        p = self.val[self.parent(i)]
        if self.isGreater(p, v):
            self.float(i)
        self.sink(i)
        return val

    def pop(self, val):
        if len(self.val) == 0:
            return None
        i = self.find(val)
        if i is None:
            print 'Error poping', val, ', does not exist in the heap.'
            return None
        self.popAt(i)

    def popInsert(self, val):
        if len(self.recent)+1 > self.k:
            j = self.recent.pop(0)
            self.popAt(j)
        i = self.insert(val)
        self.recent.append(i)
        # print 'recently inserted', [self.val[pos] for pos in self.recent]
        return i

class MaxHeap(Heap):
    def __init__(self, sz=1, k=1):
        isGreater = lambda a, b: a < b
        super(MaxHeap, self).__init__(isGreater, sz, k)


test = Solution()
print test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) # [3,3,5,5,6,7]
print test.maxSlidingWindow([9,11], 2) # [11]
print test.maxSlidingWindow([4,-2], 2) # [4]
print test.maxSlidingWindow([7,2,4], 2) # [7,4]
print test.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5) # [10,10,9,2]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10], 3) # [10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8]
print test.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10], 3) # [10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10]
print test.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4) # [7,7,7,7,7]
