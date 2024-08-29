class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        self.stones = stones
        self.sz = len(stones)
        self.visited = [False]*self.sz
        groups = self.getGroups()
        res = 0
        for g in groups:
            res += len(g) - 1
        return res
    
    def getGroups(self):
        groups = []
        for i, s in enumerate(self.stones):
            if self.visited[i]:
                continue
            group = self.dfs(s)
            for j in group:
                self.visited[j] = True
            groups.append(group)
        return groups
    
    def dfs(self, s):
        res = []
        for j, t in enumerate(self.stones):
            if self.visited[j]:
                continue
            if t[0] == s[0] or t[1] == s[1]:
                res.append(j)
                self.visited[j] = True
                res += self.dfs(t)
        return res
