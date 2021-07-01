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
        for num in nums[:k]:
            self.heap.insert(num)
        res[0] = self.heap.val[0]

        i = 1
        for num in nums[k:]:
            self.heap.pop(nums[i-1])
            self.heap.insert(num)
            res[i] = self.heap.val[0]
            i += 1
        return res

class Heap(object):
    def __init__(self, isGreater, sz=1):
        self.val = [None]*sz
        self.d = {}
        self.size = 0
        self.isGreater = isGreater

    def parent(self, i):
        return (i-1)/2

    def child(self, i):
        return 2*i + 1, 2*i + 2

    def swap(self, i, j):
        try:
            di = self.d[self.val[i]]
            di[di.index(i)] = j
        except:
            pass
        try:
            dj = self.d[self.val[j]]
            dj[dj.index(j)] = i
        except:
            pass

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
        if self.d.get(val) is None:
            self.d[val] = [i]
        else:
            self.d[val].append(i)
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
        i = self.d[val].pop()
        self.popAt(i)

class MaxHeap(Heap):
    def __init__(self, sz=1):
        isGreater = lambda a, b: a < b
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