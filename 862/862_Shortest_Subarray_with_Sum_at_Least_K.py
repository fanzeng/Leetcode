from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        res = float('inf')
        dq = deque([(0, -1)])  # Initialize with (partial sum, index)
        ps = 0  # partial sum
        for i, n in enumerate(nums):
            ps += n
            while dq and ps - dq[0][0] >= k:
                res = min(res, i - dq.popleft()[1])
            while dq and ps <= dq[-1][0]:
                dq.pop()
            dq.append((ps, i))
        return res if res != float('inf') else -1

# Monotonic stack solution (TLE)
# TLE is because the stack slicing: stack = stack[:firstGeq]
# can be an O(n) operation.
#
# class Solution(object):
#     def shortestSubarray(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         res = -1
#         stack = [] 
#         ps = 0  # partial sum
#         for i, n in enumerate(nums):
#             ps += n
#             at_most = ps - k
#             # print 'i =', i, 'at_most =', at_most
#             if len(stack) == 0:
#                 start = -1
#             else:
#                 # j = len(stack) - 1
#                 # while j >= 0 and stack[j][0] > at_most:
#                 #     j -= 1
#                 firstGreater = self.findFirstGreater(stack, 0, len(stack), at_most)
#                 if firstGreater == 0:
#                     start = -1
#                 else:
#                     start = stack[firstGreater-1][1]
#             # print 'start =', start
#             # while len(stack) > 0 and stack[-1][0] >= ps:
#             #     stack = stack[:-1]
#             firstGeq = self.findFirstGeq(stack, 0, len(stack), ps)
#             stack = stack[:firstGeq]
#             stack.append((ps, i))
#             # print stack
#             if start == -1 and ps < k:
#                 continue
#             width = i - start
#             if res == -1 or width < res:
#                 res = width
#         return res

#     # Given non-decreasing arr of tuple (a0, a1),
#     # Find index of earliest element with a0 greater than v
#     def findFirstGreater(self, arr, l, r, v):
#         while l < r:
#             m = (l + r) / 2
#             if arr[m][0] <= v:
#                 l = m + 1
#             else:
#                 r = m
#         return l

#     # Given non-decreasing arr of tuple (a0, a1),
#     # Find index of earliest element with a0 greater than or equal to v
#     def findFirstGeq(self, arr, l, r, v):
#         while l < r:
#             m = (l + r) / 2
#             if arr[m][0] < v:
#                 l = m + 1
#             else:
#                 r = m
#         return l
