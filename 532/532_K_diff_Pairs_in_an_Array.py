class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        set_res = set()
        d = {}
        for i in xrange(len(nums)):
            if d.get(nums[i]+k) is None:
                d[nums[i]+k] = [i]
            else:
                d[nums[i]+k].append(i)
            if d.get(nums[i]-k) is None:
                d[nums[i]-k] = [i]
            else:
                d[nums[i]-k].append(i)
        # print d
        for j in xrange(len(nums)):
            if d.get(nums[j]) is not None:
                for i in d.get(nums[j]):
                    if i == j:
                        continue
                    set_res.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
        return len(set_res)

test = Solution()
print test.findPairs([3,1,4,1,5], 2) # 2
print test.findPairs([1,2,3,4,5], 1) # 4
print test.findPairs([1,3,1,5,4], 0) # 1
print test.findPairs([1,2,4,4,3,3,0,9,2,3], 3) # 2
print test.findPairs([-1,-2,-3], 1) # 2
