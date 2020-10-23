class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, num in enumerate(nums):
            three = num
            # print 'three =', three
            segment_one = nums[:max(0,i)]
            segment_two = nums[i+1:]
            if len(segment_one) < 1:
                continue
            one = min(segment_one)
            # print 'one =', one
            if one >= three:
                continue
            two_exist = self.isTwoExist(segment_two, one, three)
            if two_exist:
                return True
        return False

    def isTwoExist(self, arr, one, three):
        for n in arr:
            if n > one and n < three:
                return True
        return False

test = Solution()
print test.find132pattern([1,2,3,4]) # False
print test.find132pattern([1,1,1,1]) # False
print test.find132pattern([1,2,1,2]) # False
print test.find132pattern([1,2,1,3]) # False

print test.find132pattern([3,1,4,2]) # True
print test.find132pattern([-1,3,2,0]) # True
print test.find132pattern([1,4,0,-1,-2,-3,-1,-2]) # True