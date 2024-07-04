import heapq

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.n = len(board)
        self.board = board
        self.dist = [] # steps required from 1 to this position
        self.visited = {}
        return self.doMove()

    def doMove(self):
        heapq.heappush(self.dist, (0, 1))
        self.visited[1] = True
        while len(self.dist) > 0:
            d, curr = heapq.heappop(self.dist)
            # print curr
            for i in range(1, 7):
                nxt = curr + i
                if nxt == self.n ** 2:
                    return d + 1
                if self.getBoard(nxt) != -1:
                    nxt = self.getBoard(nxt)
                    if nxt == self.n ** 2:
                        return d + 1
                if self.visited.get(nxt) is None:
                    heapq.heappush(self.dist, (d + 1, nxt))
                    self.visited[nxt] = True
        return -1

    # converts n to board value
    def getBoard(self, curr):
        row = self.n - 1 - (curr - 1) / self.n
        col = self.n - 1 - (curr - 1) % self.n if ((curr - 1) / self.n) % 2 == 1 else (curr - 1) % self.n
        return self.board[row][col]
