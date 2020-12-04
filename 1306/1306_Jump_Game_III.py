class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        self.arr = arr
        self.d = {}
        self.jump(start)
        # print self.d
        for id in xrange(len(arr)):
            if arr[id] == 0:
                if self.canReachId(id):
                    return True
        return False

    def jump(self, id):
        if self.d.get(id) is not None:
            return
        if id < 0 or id >= len(self.arr):
            return
        self.d[id] = True
        self.jump(id + self.arr[id])
        self.jump(id - self.arr[id])

    def canReachId(self, id):
        if self.d.get(id) is not None:
            return True
        return False

test = Solution()
print test.canReach([4,2,3,0,3,1,2], 5) # True
print test.canReach([4,2,3,0,3,1,2], 0) # True
print test.canReach([3,0,2,1,2], 2) # False
print test.canReach([0,3,0,6,3,3,4], 6) # True