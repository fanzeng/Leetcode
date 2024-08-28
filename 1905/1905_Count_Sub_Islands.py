class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        if grid1 is None or len(grid1) == 0:
            return 0
        self.m = len(grid1)
        self.n = len(grid1[0])
        self.g1 = grid1
        self.g2 = grid2
        self.visited =[[]]*self.m
        for i in range(self.m):
            self.visited[i] = [False]*self.n
        return self.getIslands()

    def getIslands(self):
        s = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.visited[i][j]:
                    continue
                if self.g2[i][j] == 1:
                    island = self.dfs(i, j, [])
                    # print island
                    s += 1 if self.validate(island) else 0
        return s
    
    def dfs(self, i, j, a):
        self.visited[i][j] = True
        a.append((i,j))
        if i > 0 and not self.visited[i-1][j] and self.g2[i-1][j] == 1:
            a = self.dfs(i-1, j, a)
        if j > 0 and not self.visited[i][j-1] and self.g2[i][j-1] == 1:
            a = self.dfs(i, j-1, a)
        if i < self.m-1 and not self.visited[i+1][j] and self.g2[i+1][j] == 1:
            a = self.dfs(i+1, j, a)
        if j < self.n-1 and not self.visited[i][j+1] and self.g2[i][j+1] == 1:
            a = self.dfs(i, j+1, a)
        return a
            
    def validate(self, island):
        for i, j in island:
            if self.g1[i][j] != 1:
                return False
        return True
