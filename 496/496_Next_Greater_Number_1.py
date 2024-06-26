class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Notice that if num_i sits before num_j in num2, and num_i > num_j,
        # then num_j will never be the "next great" for any number before num_i.
        # Not sure if that's useful but just noting that down.

        # use deque to impl a stack
        from collections import deque
        d = {}
        stack = deque()
        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                f = stack.pop()
                d[f] = num
            stack.append(num)
        # print d
        return [d[num] if d.get(num) is not None else -1 for num in nums1]
