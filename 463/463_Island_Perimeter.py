class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p = 0
        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                if grid[r][c] == 0:
                    p += self.countNeighboringOnes(grid, r, c)
        for r in xrange(len(grid)):
            p += grid[r][0] + grid[r][-1]
        for c in xrange(len(grid[0])):
            p += grid[0][c] + grid[-1][c]
        return p


    def countNeighboringOnes(self, grid, r, c):
        count = 0
        if r-1 >= 0:
            count += grid[r-1][c]
        if r+1 < len(grid):
            count += grid[r+1][c]
        if c-1 >= 0:
            count += grid[r][c-1]
        if c+1 < len(grid[0]):
            count += grid[r][c+1]
        return count


test = Solution()
print test.islandPerimeter(
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
) # 16