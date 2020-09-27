class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        sorted_nums =  sorted(nums, reverse=True, cmp=lambda a, b: self.isStrGreater(str(a), str(b)))
        res = ''.join([str(x) for x in sorted_nums])
        if int(res) == 0:
            return '0'
        else:
            return res

    def isStrGreater(self, a, b):
        is_str_greater_1 = self.isStrGreater1(a, b)
        if is_str_greater_1 == 0:
            # print 'equal'
            return int(a+b) - int(b+a)
        else:
            return is_str_greater_1

    def isStrGreater1(self, a, b):
        if len(a) == len(b):
            return int(a) - int(b)
        elif len(a) < len(b):
            return self.isStrGreater1(a + b[0], b)
        else:
            return self.isStrGreater1(a, b + a[0])

test = Solution()
print test.largestNumber([10,2]) # "210"
print test.largestNumber([3,30,34,5,9]) # "9534330"
print test.largestNumber([121,12]) # "12121"
print test.largestNumber([0,0]) # "0"

