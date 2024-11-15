class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        firstDecrease = len(arr)
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < prev:
                firstDecrease = i
                break
            prev = arr[i]
        # print firstDecrease
        if firstDecrease == len(arr):
            return 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < arr[i-1]:
                lastDecrease = i
                break
        # print lastDecrease
        res = lastDecrease
        for start in range(1, firstDecrease+1):
            v = arr[start-1]
            end = self.findFirstGeq(arr, lastDecrease, len(arr), v)
            # print start, end
            res = min(res, end - start)
        return res

    def findFirstGeq(self, arr, l, r, v):
        while l < r:
            m = (l + r) / 2
            if arr[m] < v:
                l = m + 1
            else:
                r = m
        return l
