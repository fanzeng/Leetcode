class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0, 1]
        while len(res) <= num:
            res += [1] + [r+1 for r in res[1:]]
        return res[:num+1]

test = Solution()
print test.countBits(2) # [0,1,1]
print test.countBits(5) # [0,1,1,2,1,2]
print test.countBits(15) # [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
print test.countBits(25) # [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3]