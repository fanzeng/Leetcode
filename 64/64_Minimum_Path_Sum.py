class Solution(object):
    def __init__(self):
        self.d = {}

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return grid[0][0] + self.minPathSumDP(grid, 0, 0)

    def minPathSumDP(self, grid, i, j):
        h = len(grid)
        w = len(grid[0])
        key = str(i) + '_' + str(j)
        val = self.d.get(key)
        if val is not None:
            return val
        if i == h - 1 and j == w - 1:
            self.d[key] = 0
            return 0
        if j == w - 1:
            val = grid[i+1][j] + self.minPathSumDP(grid, i+1, j)
            self.d[key] = val
            return val
        if i == h - 1:
            val = grid[i][j + 1] + self.minPathSumDP(grid, i, j + 1)
            self.d[key] = val
            return val

        path_sum_right = grid[i][j+1] + self.minPathSumDP(grid, i, j+1)
        path_sum_bottom = grid[i+1][j] + self.minPathSumDP(grid, i+1, j)
        val = min(path_sum_right, path_sum_bottom)
        self.d[key] = val
        return val


grid_7 = [[1,3,1], [1,5,1], [4,2,1]] # 7

test = Solution()
print test.minPathSum(grid_7)
