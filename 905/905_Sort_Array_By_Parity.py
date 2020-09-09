class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for num in A:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)
        return even + odd

test = Solution()
print test.sortArrayByParity([3,1,2,4])