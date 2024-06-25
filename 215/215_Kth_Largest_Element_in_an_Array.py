class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        for num in nums:
            if d.get(num) is None:
                d[num] = 1
            else:
                d[num] += 1
        # print d.items()
        count = 0
        for key, v in sorted(d.items(), key=lambda x: -x[0]):
            count += v
            # print count, key
            if count >= k:
                return key
