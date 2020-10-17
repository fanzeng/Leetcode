class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        row_id = self.binarySearch(self.col(0), target)
        arr = self.row(row_id)
        if row_id + 1 < self.rows:
            arr += self.row(row_id+1)
        elem_id = self.binarySearch(arr, target)
        return arr[elem_id] == target or (elem_id + 1 < len(arr) and arr[elem_id+1] == target)

    def row(self, i):
        return self.matrix[i]

    def col(self, i):
        return [row[i] for row in self.matrix]

    def binarySearch(self, arr, t):
        if arr is None or len(arr) == 0:
            return 0
        l = 0
        r = len(arr)-1
        mid = (l+r)/2
        while l < r:
            if arr[mid] == t:
                return mid
            if arr[mid] < t:
                l = mid
                mid = (l+r)/2
            else:
                r = mid-1
                mid = (l+r)/2
            if l == mid:
                break
        return l

test = Solution()
print test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3) # True
print test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13) # False
print test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11) # True
print test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 19) # False
print test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 34) # True
print test.searchMatrix([], 0) # False
print test.searchMatrix([[0]], 0) # True
print test.searchMatrix([[]], 1) # False