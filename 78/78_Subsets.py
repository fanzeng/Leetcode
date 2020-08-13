class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [[]]
        for num in nums:
            self.getSubsets(num)
        return self.res

    def getSubsets(self, num):
        # print num, self.res
        res = self.res
        new_res = []
        for r in res:
            new_r = r + [num]
            new_res.append(new_r)
        self.res += new_res
        return

test = Solution()
print test.subsets([1,2,3])
print test.subsets([])
print test.subsets([1])
print len(test.subsets(xrange(10)))

