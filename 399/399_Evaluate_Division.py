class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        res = []
        self.adj = self.getAdj(equations, values)
        # print 'self.adj =', self.adj
        for query in queries:
            res.append(self.getAns(query))
        return res

    def DFS(self, s, t, prod, processed):
        adj = self.adj.get(s)
        if adj is None:
            return -1.
        for u, v in adj:
            if u == t:
                return prod*v
            if u in processed:
                continue
            processed.add(u)
            p = self.DFS(u, t, prod*v, processed)
            if p > 0:
                return p
        return -1.

    def getAns(self, query):
        s, t = query
        return self.DFS(s, t, 1., set())

    def getAdj(self, equations, values):
        adj = {}
        for e, v in zip(equations, values):
            s, t = e
            if adj.get(s) is None:
                adj[s] = [(s, 1.), (t, v)]
            else:
                adj[s].append((t, v))
            if adj.get(t) is None:
                adj[t] = [(s, 1./float(v))]
            else:
                adj[t].append((s, 1./float(v)))            
        return adj

test = Solution()
print test.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]) # [6.00000,0.50000,-1.00000,1.00000,-1.00000]
print test.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]) # [3.75000,0.40000,5.00000,0.20000]
print test.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]) # [0.50000,2.00000,-1.00000,-1.00000]
