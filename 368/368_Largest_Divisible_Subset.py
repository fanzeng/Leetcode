class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.maxCompleteSubset(nums)

    def maxCompleteSubset(self, V):
        max_size = 0
        maxCompleteSubset = []
        for v in V:
            completeSubset = self.maxCompleteSubsetSingleSource(v, V)
            # print 'completeSubset for', v, 'is', completeSubset
            if len(completeSubset) > max_size:
                max_size = len(completeSubset)
                maxCompleteSubset = completeSubset
        return maxCompleteSubset

    def maxCompleteSubsetSingleSource(self, s, V):
        completeSubset = [s]
        adj = self.getAdj(V)
        if adj.get(s) is None:
            return completeSubset
        return [s] + self.largestDivisibleSubset(adj.get(s))


    def hasEdge(self, a, b):
        return a % b == 0 or b % a == 0

    def getAdj(self, V):
        adj = {}
        for s in V:
            adj[s] = []
            for v in V:
                if v == s:
                    continue
                if self.hasEdge(v, s):
                    adj[s].append(v)
        return adj

test = Solution()
print test.largestDivisibleSubset([1,2,3]) # [1, 2] or [1, 3]
print test.largestDivisibleSubset([1,2,4,8]) # [1,2,4,8]
print test.largestDivisibleSubset([3,4,8,16]) # [4,8,16]
