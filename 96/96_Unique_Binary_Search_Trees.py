class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = {}
        return self.numTreesRecursive(range(1, n+1))

    def numTreesRecursive(self, arr):
        if self.d.get(self.getHash(arr)) is not None:
            return self.d.get(self.getHash(arr))
        if arr is None or len(arr) == 0:
            return 1
        count = 0
        for n in arr:
            arr_l = [x for x in arr if x < n]
            arr_r = [x for x in arr if x > n]
            # print n, arr_l, arr_r
            count += self.numTreesRecursive(arr_l)*self.numTreesRecursive(arr_r)
        self.d[self.getHash(arr)] = count
        return count

    def getHash(self, arr):
        # s = ''
        # for n in arr:
        #     s += str(n) + '.'
        # return s
        return hash(tuple(arr))

test = Solution()
print test.numTrees(3) # 5