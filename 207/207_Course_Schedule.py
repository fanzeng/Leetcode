class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.adj = self.listEdgeToAdjacencyList(prerequisites)
        # print self.adj
        self.has_loop = False
        self.finished = []
        self.doing = []
        for v in xrange(numCourses):
            if v not in self.finished:
                self.doing.append(v)
                self.DFS(v)
        return not self.has_loop

    def DFS(self, v):
        if self.adj.get(v) is not None:
            for u in self.adj.get(v):
                if u in self.doing:
                    self.has_loop = True
                    return
                if u not in self.finished:
                    self.doing.append(u)
                    self.DFS(u)
        self.doing.remove(v)
        self.finished.append(v)

    def listEdgeToAdjacencyList(self, list_edge):
        adj = {}
        for edge in list_edge:
            adj_res = adj.get(edge[0])
            if adj_res is None:
                adj[edge[0]] = [edge[1]]
            else:
                adj[edge[0]].append(edge[1])
        return adj



test = Solution()
print test.canFinish(2, [[1,0]]) # True
print test.canFinish(2, [[1,0],[0,1]]) # False
print test.canFinish(2, [[0,1],[1,2],[2,3],[3,0]]) # False
print test.canFinish(6, [[0,1],[1,2],[1,3],[1,4],[2,5],[3,4],[5,4]]) # True
print test.canFinish(6, [[0,1],[1,2],[1,3],[1,4],[2,5],[3,4],[4,0],[5,4]]) # False