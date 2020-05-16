class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) == 1:
            return A[0]
        else:
            max_sum_normal = self.maxSubarray(A)
            min_sum_center = -self.maxSubarray([-x for x in A[1:-1]])
            max_sum_circ = sum(A) - min_sum_center
            return max(max_sum_normal, max_sum_circ)

    def maxSubarray(self, A):
        sum_since_reset = A[0]
        max_sum = sum_since_reset
        for i in range(1, len(A)):
            sum_since_reset += A[i]
            if A[i] > sum_since_reset:
                sum_since_reset = A[i]
            max_sum = max(max_sum, sum_since_reset)
        return max_sum

test = Solution()
print test.maxSubarraySumCircular([1,-2,3,-2]) # 3
print test.maxSubarraySumCircular([5,-3,5]) # 10
print test.maxSubarraySumCircular([3,-1,2,-1]) # 4
print test.maxSubarraySumCircular([3,-2,2,-3]) # 3
print test.maxSubarraySumCircular([-2,-3,-1]) # -1
print test.maxSubarraySumCircular([2,-2,2,7,8,0]) # 19
print test.maxSubarraySumCircular([9,7,-6,7,9,-10,5,9,0,-1]) # 39

