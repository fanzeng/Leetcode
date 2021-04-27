class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        self.heights = heights
        self.d = {}
        return self.furthestBuildingDP(0, bricks, ladders)

    def furthestBuildingDP(self, pos, bricks, ladders):
        res = self.d.get((pos, bricks, ladders))
        if res is not None:
            return res
        if ladders >= len(self.heights)-1-pos:
            return len(self.heights)-1
        if pos == len(self.heights)-1 or (bricks < (self.heights[pos+1]-self.heights[pos]) and ladders == 0):
            self.d[(pos, bricks, ladders)] = pos
            return pos
        if self.heights[pos] >= self.heights[pos+1]:
            res = self.furthestBuildingDP(pos + 1, bricks, ladders)
            self.d[(pos, bricks, ladders)] = res
            return res
        if bricks < (self.heights[pos+1]-self.heights[pos]):
            res = self.furthestBuildingDP(pos+1, bricks, ladders-1)
            self.d[(pos, bricks, ladders)] = res
            return res
        if ladders == 0:
            return self.furthestBuildingDP(pos+1, bricks-(self.heights[pos+1]-self.heights[pos]), ladders)
        res = max(
            self.furthestBuildingDP(pos+1, bricks, ladders-1),
            self.furthestBuildingDP(pos+1, bricks-(self.heights[pos+1]-self.heights[pos]), ladders)
        )
        self.d[(pos, bricks, ladders)] = res
        return res

test = Solution()
print test.furthestBuilding([4,2,7,6,9,14,12], 5, 1) # 4
print test.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) # 7
print test.furthestBuilding([14,3,19,3], 17, 0) # 3