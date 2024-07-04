import heapq
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        self.pq = []
        visited = {}
        heapq.heappush(self.pq, (0, startGene))
        while self.pq:
            dist, g = heapq.heappop(self.pq)
            for gene in bank:
                if visited.get(gene) is not None:
                    continue
                if self.isMutate(g, gene):
                    if gene == endGene:
                        return dist + 1
                    heapq.heappush(self.pq, (dist+1, gene))
                    visited[gene] = True
        return -1
    
    def isMutate(self, a, b):
        if len(a) != len(b):
            return False
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 1
