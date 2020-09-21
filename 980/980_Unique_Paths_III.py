class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.count_valid = 0
        self.start, self.end = self.findStartEnd(grid)
        self.h = len(grid)
        self.w = len(grid[0])
        # print self.start, self.end, self.count_valid
        self.l_path = []
        self.walkDP(self.start[0], self.start[1], [self.start])
        return len(self.l_path)

    def walkDP(self, row, col, prev):
        if (row, col) == self.end:
            # print prev
            if len(prev) == 2 + self.count_valid:
                self.l_path.append(prev)
        l_neighbors = self.getNeighbors(row, col)
        for n in l_neighbors:
            if self.grid[n[0]][n[1]] == -1 or n in prev:
                continue
            self.walkDP(n[0], n[1], prev + [n])

    def findStartEnd(self, grid):
        start = ()
        end = ()
        for i, row in enumerate(grid):
            for j, square in enumerate(row):
                if square == 1:
                    start = (i, j)
                elif square == 2:
                    end = (i, j)
                elif square == 0:
                    self.count_valid += 1
        return start, end

    def getNeighbors(self, row, col):
        l_neighbors = []
        if row - 1 >= 0:
            l_neighbors.append((row-1, col))
        if col - 1 >= 0:
            l_neighbors.append((row, col-1))
        if row + 1 < self.h:
            l_neighbors.append((row+1, col))
        if col + 1 < self.w:
            l_neighbors.append((row, col+1))
        return l_neighbors

test = Solution()
print test.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) # 2
print test.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) # 4
print test.uniquePathsIII([[0,1],[2,0]]) # 0