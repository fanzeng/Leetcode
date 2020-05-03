class Solution(object):
    def subarraySum(self, nums, k):
        self.d = {}
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            # print 'nums[i]=', nums[i], 'sum=', sum
            if self.d.get(sum) is None:
                self.d[sum] = 1
            else:
                self.d[sum] = self.d.get(sum) + 1
        # print self.d

        ans = 0
        sum = 0
        d_i = {}
        for i in xrange(len(nums)-1):
            # print 'i =', i, ',nums[i] =', nums[i]
            if nums[i] == k:
                ans += 1
                # print '+ 1: nums[', i, '] = k'
            sum += nums[i]
            if d_i.get(sum) is None:
                d_i[sum] = 1
            else:
                d_i[sum] = d_i[sum] + 1

            complement = k - nums[i]
            key = complement + sum

            d_whole_res = self.d.get(key)
            if d_whole_res is not None:
                # print 'd_whole[', key, '] =', d_whole_res
                pass
            else:
                d_whole_res = 0
                # print 'd_whole[', key, '] = 0'

            d_i_res = d_i.get(key)
            if d_i_res is not None:
                # print 'd_i[', key, '] =', d_i_res
                pass
            else:
                d_i_res = 0
                # print 'd_i[', key, '] = 0'


            if d_whole_res - d_i_res > 0:
                ans += d_whole_res - d_i_res
                # print '+', d_whole_res- d_i_res

        if nums[-1] == k:
            ans += 1
            # print '+1: i =', len(nums)-1, ', num[-1] == k'
        return ans

# brute force solution: TLE
    # def subarraySum(self, nums, k):
    #     ans = 0
    #     for i in xrange(0, len(nums)):
    #         sum = nums[i]
    #         if sum == k:
    #             ans += 1
    #         for j in xrange(i+1, len(nums)):
    #             sum += nums[j]
    #             if sum == k:
    #                 ans += 1
    #     return ans

# inefficient DP solution: TLE
# due to difference in k in recursive call, the hit rate of dictionary result can be low.
    # def subarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     self.d = {}
    #     ans = 0
    #     for i in xrange(len(nums)-1):
    #         key = self.get_key(i+1, k-nums[i])
    #         d_res = self.d.get(key)
    #         if d_res is None:
    #             res = self.subarraySumDP(nums, i+1, len(nums), k-nums[i])
    #             self.d[key] = res
    #         else :
    #             res = d_res
    #         ans += res
    #     if nums[-1] == k:
    #         ans += 1
    #     # print self.d
    #     return ans
    #
    #
    # def subarraySumDP(self, nums, start, end, k):
    #     # print 'in subarraySumDP: ', start, end, k
    #     key = self.get_key(start, k)
    #     d_res = self.d.get(key)
    #     if d_res is not None:
    #         return d_res
    #     ans = 0
    #     if k == 0:
    #         ans += 1
    #         # print '+1 : k == 0'
    #     if start == end-1:
    #         if nums[start] == k:
    #             ans += 1
    #             # print '+1 : nums[start] == k'
    #
    #         self.d[key] = ans
    #         return ans
    #     key = self.get_key(start+1, k-nums[start])
    #     res = self.d.get(key)
    #     if res is None:
    #         res = self.subarraySumDP(nums, start + 1, end, k - nums[start])
    #         self.d[key] = res
    #     ans += res
    #     key = self.get_key(start, k)
    #     self.d[key] = ans
    #     return ans
    #
    # def get_key(self, start, k):
    #     return str(start) + '_' + str(k)

test = Solution()

print test.subarraySum([1,1,1], 2) # 2
print '\n'

print test.subarraySum([1,2,3], 3) # 2
print '\n'

print test.subarraySum([3,2,3], 3) # 2
print '\n'

print test.subarraySum([1], 0) # 0
print '\n'

print test.subarraySum([-1,-1,1], 0) # 1
print '\n'

print test.subarraySum([-1,1,-1,1], 0) # 4
print '\n'
