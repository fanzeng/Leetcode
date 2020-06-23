class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        self.dungeon = dungeon
        self.d_hp = {}
        self.h = len(dungeon)
        self.w = len(dungeon[0])
        self.d_hp[self.getHash(self.h - 1, self.w - 1)] = max(1, 1 - self.dungeon[-1][-1])
        return self.minHPDP(0, 0)

    def minHPDP(self, r, c):
        d_res = self.d_hp.get(self.getHash(r, c))
        if d_res is not None:
            return d_res
        room = self.dungeon[r][c]
        if c == self.w - 1:
            hp = max(1, 1-room, self.minHPDP(r+1, c) - room)
        elif r == self.h - 1:
            hp = max(1, 1-room, self.minHPDP(r, c+1) - room)
        else:
            res_right = max(1, 1-room, self.minHPDP(r, c+1) - room)
            res_down = max(1, 1-room, self.minHPDP(r+1, c) - room)
            hp = min(res_right, res_down)
        self.d_hp[self.getHash(r, c)] = hp
        return hp

    def getHash(self, r, c):
        return r*self.w + c

d0 = [
    [-2, -3, 3],
    [-5, -10, 1],
    [-10, 30, -5]
]
test = Solution()
print test.calculateMinimumHP(d0) # 7