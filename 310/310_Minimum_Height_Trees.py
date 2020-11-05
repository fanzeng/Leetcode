class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0:
            return None
        self.n = n
        self.edges = edges
        self.getAdj()
        # print 'self.adj =',self.adj
        self.d = {}
        self.d_res = {}
        for v in xrange(self.n):
            height = self.getHeight(v, 1, {v})
            if self.d_res.get(height) is None:
                self.d_res[height] = [v]
            else:
                self.d_res[height].append(v)
        # print self.d_res
        return self.d_res[min(self.d_res.keys())]

    def getHeight(self, v, height, used):
        adj = self.adj.get(v)
        if adj is None:
            return height
        adj = [n for n in adj if n not in used]
        h = self.getHash(v, adj)
        # print 'h =', h
        if self.d.get(h) is not None:
            return self.d[h] + height
        next_height = height
        for u in adj:
            used.add(u)
            next_height = max(next_height, self.getHeight(u, height+1, used))
        self.d[h] = next_height - height
        return next_height

    def getAdj(self):
        self.adj = {}
        for edge in self.edges:
            a, b = edge
            if self.adj.get(a) is None:
                self.adj[a] = [b]
            else:
                self.adj[a].append(b)
            if self.adj.get(b) is None:
                self.adj[b] = [a]
            else:
                self.adj[b].append(a)

    def getHash(self, u, used):
        h = str(u) + ';'
        for u in sorted(used):
            h += str(u) + ','
        return h


test = Solution()
print test.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) # [1]
print test.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]) # [3,4]
print test.findMinHeightTrees(1, []) # [0]
print test.findMinHeightTrees(2, [[0,1]]) # [0,1]
print test.findMinHeightTrees(
    126,
    [[0,1],[1,2],[1,3],[0,4],[3,5],[3,6],[3,7],[0,8],[0,9],[0,10],[1,11],[0,12],[6,13],[7,14],[3,15],[2,16],[0,17],[8,18],[10,19],[0,20],[16,21],[18,22],[3,23],[19,24],[7,25],[2,26],[13,27],[3,28],[25,29],[20,30],[5,31],[7,32],[32,33],[29,34],[3,35],[22,36],[21,37],[37,38],[3,39],[31,40],[34,41],[21,42],[40,43],[3,44],[7,45],[25,46],[4,47],[41,48],[17,49],[27,50],[28,51],[17,52],[36,53],[3,54],[37,55],[37,56],[4,57],[10,58],[12,59],[33,60],[33,61],[23,62],[3,63],[13,64],[29,65],[2,66],[31,67],[25,68],[16,69],[4,70],[67,71],[36,72],[54,73],[18,74],[31,75],[75,76],[59,77],[33,78],[2,79],[45,80],[53,81],[8,82],[63,83],[40,84],[44,85],[36,86],[33,87],[83,88],[83,89],[49,90],[16,91],[75,92],[32,93],[19,94],[22,95],[58,96],[72,97],[14,98],[17,99],[12,100],[77,101],[54,102],[21,103],[103,104],[79,105],[53,106],[77,107],[75,108],[22,109],[80,110],[92,111],[76,112],[64,113],[16,114],[10,115],[89,116],[93,117],[13,118],[113,119],[9,120],[30,121],[17,122],[86,123],[39,124],[104,125]]
) # [1]