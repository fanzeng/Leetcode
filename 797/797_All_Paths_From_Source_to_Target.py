class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graph = graph
        self.d = {}
        self.res = []
        self.target = len(graph)-1
        if len(graph) == 0:
            return []
        self.DFS(0, [])
        return self.res

    def DFS(self, v, path):
        if v == self.target:
            self.res.append(path + [v])
        for u in self.graph[v]:
            self.DFS(u, path + [v])

test = Solution()
print test.allPathsSourceTarget([[1,2], [3], [3], []]) # [[0,1,3],[0,2,3]]
print test.allPathsSourceTarget([]) # []