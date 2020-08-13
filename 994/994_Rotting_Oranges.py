class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        time = 0
        while self.hasFreshOrange():
            time += 1
            changed = self.nextMinute()
            # self.visualize(time)
            if not changed:
                return -1
        return time

    def nextMinute(self):
        changed = False
        for r, row in enumerate(self.grid):
            for c, orange in enumerate(row):
                if orange == 2:
                    if self.rot(r, c):
                        changed = True
        for r in xrange(len(self.grid)):
            for c in xrange(len(self.grid[0])):
                self.grid[r][c] = min(2, self.grid[r][c])
        return changed

    def rot(self, r, c):
        changed = False
        if r - 1 >= 0 and self.grid[r-1][c] == 1:
            self.grid[r-1][c] = 3
            changed = True
        if r + 1 < len(self.grid) and self.grid[r+1][c] == 1:
            self.grid[r+1][c] = 3
            changed = True
        if c - 1 >= 0 and self.grid[r][c-1] == 1:
            self.grid[r][c-1] = 3
            changed = True
        if c + 1 < len(self.grid[0]) and self.grid[r][c+1] == 1:
            self.grid[r][c+1] = 3
            changed = True
        return changed

    def hasFreshOrange(self):
        for row in self.grid:
            if 1 in row:
                return True
        return False

    def visualize(self, time):
        print 'time =', time
        for row in self.grid:
            print row

test = Solution()
print test.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) # 4
print test.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) # -1
print test.orangesRotting([[0,2]]) # 0