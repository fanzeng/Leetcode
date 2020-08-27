class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        self.res = []
        self.d_begin = {}
        for i, intv in enumerate(intervals):
            self.d_begin[intv[0]] = i
        sorted_keys = sorted(self.d_begin.keys())
        for intv in intervals:
            end = intv[1]
            min_key = self.findNoSmallerBinarySearch(sorted_keys, end)
            if min_key is None:
                self.res.append(-1)
            else:
                self.res.append(self.d_begin[min_key])
        return self.res

    def findNoSmallerBinarySearch(self, array, key):
        if array is None or len(array) == 0:
            return None
        if len(array) == 1:
            if array[0] >= key:
                return array[0]
            else:
                return None
        l = 0
        r = len(array) - 1
        m = (l + r) / 2
        if array[m] == key:
            return key
        if array[m] > key:
            return self.findNoSmallerBinarySearch(array[:m+1], key)
        else:
            return self.findNoSmallerBinarySearch(array[m+1:], key)

test = Solution()
print test.findRightInterval([[1,2]]) # [-1]
print test.findRightInterval([[3,4],[2,3],[1,2]]) # [-1,0,1]
print test.findRightInterval([[1,4],[2,3],[3,4]]) # [-1,2,-1]
print test.findRightInterval([]) # []
print test.findRightInterval([[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]) # [3,3,3,4,5,-1]