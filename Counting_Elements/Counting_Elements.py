class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = {}
        for num in arr:
            d[num-1] = True
        count = 0
        for num in arr:
            if d.get(num):
                count += 1
        return count
test = Solution()
print test.countElements([1,1,3,3,5,5,7,7]) # 0
print test.countElements([1,1,3,3,5,5,7,7]) # 0
print test.countElements([1,3,2,3,5,0]) # 3
print test.countElements([1,1,2,2]) # 2

# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.
# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000