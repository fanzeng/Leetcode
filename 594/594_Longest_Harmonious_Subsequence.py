class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if d.get(num) is None:
                d[num] = 1
            else:
                d[num] += 1
        # print d
        lhs = 0
        for num, count in d.items():
            if d.get(num+1) is not None:
                # print num, count
                lhs = max(lhs, count + d.get(num+1))
        return lhs

test = Solution()
print test.findLHS([1,3,2,2,5,2,3,7]) # 5
print test.findLHS([1,2,3,4]) # 2
print test.findLHS([1,1,1,1]) # 0
print test.findLHS([]) # 0