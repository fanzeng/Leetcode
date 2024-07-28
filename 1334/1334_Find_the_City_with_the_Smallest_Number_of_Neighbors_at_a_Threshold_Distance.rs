class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        self.e = {}
        self.build_adj(edges)
        # print self.e
        cities = range(0, n)
        self.d = dict.fromkeys(cities)
        for k in self.d:
            self.d[k] = set()
        for city in cities[:]:
            self.dfs(city, city, distanceThreshold, {})
        # print self.d
        min_size = min([len(v) for v in self.d.values()])
        # print min_size
        return max([k for k in cities if len(self.d.get(k)) == min_size])

    def dfs(self, src, n, t, p):
        # print src, n, t
        if self.e.get(n) is None:
            return
        for (u, w) in self.e[n]:
            if u != src and w <= t:
                if w < t:
                    # print p
                    if p.get(u) is None or p[u] < t - w:
                        p[u] = t - w
                        self.dfs(src, u, t - w, p) 
                self.d[src].add(u)

    def build_adj(self, edges):
        for (u, v, w) in edges:
            if self.e.get(u) is None:
                self.e[u] = [(v, w)]
            else:
                self.e[u].append((v, w))
            if self.e.get(v) is None:
                self.e[v] = [(u, w)]
            else:
                self.e[v].append((u, w))
