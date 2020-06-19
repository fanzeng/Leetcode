class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        self.adj = self.listEdgeToAdjacencyListBidirectional(dislikes)
        # print self.adj
        if N < 3 or len(self.adj) == 0:
            return True
        self.d_color = {}
        self.l_finished = []
        self.possible = True
        for i in xrange(1, N):
            if self.possible:
                if self.d_color.get(i) is None:
                    self.colorVertices(i, 0)
                else:
                    self.colorVertices(i, self.d_color.get(i))
            else:
                break
        # print 'self.d_color =', self.d_color
        # print 'self.l_finished =', self.l_finished
        return self.possible

    def colorVertices(self, v, color):
        if self.d_color.get(v) is None:
            self.d_color[v] = color
            if self.adj.get(v) is not None:
                for u in self.adj.get(v):
                    self.colorVertices(u, 1 - color)
            self.l_finished.append(v)
        else:
            self.possible = self.possible and self.d_color.get(v) == color
            if not self.possible:
                return

    def listEdgeToAdjacencyListBidirectional(self, list_edge):
        adj = {}
        for edge in list_edge:
            adj_res = adj.get(edge[0])
            if adj_res is None:
                adj[edge[0]] = [edge[1]]
            else:
                adj[edge[0]].append(edge[1])
            adj_res = adj.get(edge[1])
            if adj_res is None:
                adj[edge[1]] = [edge[0]]
            else:
                adj[edge[1]].append(edge[0])
        return adj

test = Solution()
print test.possibleBipartition(4, [[1,2],[1,3],[2,4]]) # True
print test.possibleBipartition(3, [[1,2],[1,3],[2,3]]) # False
print test.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]) # False
print test.possibleBipartition(10, [[6,9],[1,3],[4,8],[5,6],[2,8],[4,7],[8,9],[2,5],[5,8],[1,2],[6,7],[3,10],[8,10],[1,5],[3,6],[1,10],[7,9],[4,10],[7,10],[1,4],[9,10],[4,6],[2,7],[6,8],[5,7],[3,8],[1,8],[1,7],[7,8],[2,4]]) # False