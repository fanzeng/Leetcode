class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = []
        for num in nums:
            if num == 1:
                new_nums.append(1)
            else:
                new_nums.append(-1)
        sum_from_ends = sum(new_nums)
        # print sum_from_ends
        if sum_from_ends == 0:
            return len(new_nums)
        s = 0
        sum_from_front = []
        for i in xrange(len(new_nums)):
            s += new_nums[i]
            sum_from_front.append(s)
        # print sum_from_front
        s = 0
        sum_from_back = []
        for j in xrange(len(new_nums)-1, -1, -1):
            s += new_nums[j]
            sum_from_back.append(s)
        # print sum_from_back
        d = {}
        for j in xrange(len(sum_from_back)-1, -1, -1):
            d[sum_from_ends - sum_from_back[j]] = j
            d[sum_from_ends] = -1
        # print d
        if d.get(0) is not None:
            min_sum_index = d.get(0) + 1
        else:
            min_sum_index = 2*len(new_nums)
        for i in xrange(len(sum_from_front)):
            index_end = d.get(sum_from_front[i])
            if index_end is not None:
                sum_index = (i + 1) + (index_end + 1)
                # print i, index_end, sum_index
                if sum_index < min_sum_index:
                    min_sum_index = sum_index
        return len(new_nums) - min_sum_index


test = Solution()
print test.findMaxLength([0, 1]) # 2
print test.findMaxLength([0, 1, 0]) # 2
print test.findMaxLength([0, 1, 1, 0, 0, 0, 1, 0, 0, 0]) # 6
print test.findMaxLength([0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0]) # 4
print test.findMaxLength([0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1]) # 4
print test.findMaxLength([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]) # 8
print test.findMaxLength([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) # 10
print test.findMaxLength([1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]) # 12

# Note: The length of the given binary array will not exceed 50,000.

