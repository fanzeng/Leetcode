import math

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # magicNumber is a binary number of max(nums) bits
        # toggle bit abs(n) for each n
        # the singled-out number will leave the only "set" bit after one pass over the list
        magicNumber = 0
        for n in nums:
            magicNumber ^= 2**abs(n)
        res_abs = int(math.log(magicNumber, 2))
        if res_abs == 0:
            return 0
        pos = 0
        neg = 0
        for n in nums:
            if n == res_abs:
                if n > 0:
                    pos += 1
                else:
                    neg += 1

        if pos % 2 == 0:
            return -res_abs
        else:
            return res_abs

test = Solution()
print test.singleNumber([2,2,1])
print test.singleNumber([4,1,2,1,2])
print test.singleNumber([1])
print test.singleNumber([-1])
print test.singleNumber([0])
print test.singleNumber([1,3,1,-1,3])
print test.singleNumber([10,30,10,40,30])
print test.singleNumber([-1, 0, 1, -1, 1])
print test.singleNumber([2000, 2004, 2020, 2020, 2000])
print test.singleNumber([-2000, -2004, 2020, 2020, -2000])
print test.singleNumber([2000, 2004, 2020, 2020, 2008, 2008, 2000])


# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4