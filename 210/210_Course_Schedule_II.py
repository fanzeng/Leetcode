class Solution(object):
    def findOrder(self, numCourses, prerequisites):
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
        if self.has_loop:
            return []
        else:
            return self.finished

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
print test.findOrder(2, [[1,0]]) # [0,1]
print test.findOrder(2, [[0,1],[1,0]]) # []
print test.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) # [0,1,2,3] or [0,2,1,3]