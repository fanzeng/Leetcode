class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.memoi = {}
        return self.maxCompleteSubset(nums)

    def maxCompleteSubset(self, V):
        if self.memoi.get(self.hash(V)) is not None:
            return self.memoi.get(self.hash(V))
        max_size = 0
        maxCompleteSubset = []
        remaining = V[:]
        for v in V:
            completeSubset = self.maxCompleteSubsetSingleSource(v, remaining)
            # print 'completeSubset for', v, 'is', completeSubset
            if len(completeSubset) > max_size:
                max_size = len(completeSubset)
                maxCompleteSubset = completeSubset
            remaining.remove(v)
        self.memoi[self.hash(V)] = maxCompleteSubset
        return maxCompleteSubset

    def maxCompleteSubsetSingleSource(self, s, V):
        completeSubset = [s]
        adj = self.getAdj(s, V)
        if len(adj) == 0:
            return completeSubset
        return [s] + self.maxCompleteSubset(adj)


    def hasEdge(self, a, b):
        return a % b == 0 or b % a == 0

    def getAdj(self, s, V):
        adj = []
        for v in V:
            if v == s:
                continue
            if self.hasEdge(v, s):
                adj.append(v)
        return adj

    def hash(self, l):
        s = ''
        for n in sorted(l):
            s += str(n)
            s += '.'
        return s

test = Solution()
print test.largestDivisibleSubset([1,2,3]) # [1, 2] or [1, 3]
print test.largestDivisibleSubset([1,2,4,8]) # [1,2,4,8]
print test.largestDivisibleSubset([3,4,8,16]) # [4,8,16]
