class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 2:
            return True
        if coordinates[1][0] == coordinates[0][0]:
            for coordinate in coordinates[2:]:
                if coordinate[0] != coordinates[0][0]:
                    return False
            return True
        k = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        b = coordinates[0][1] - k*coordinates[0][0]

        for coordinate in coordinates[2:]:
            if coordinate[1] != k*coordinate[0] + b:
                return False
        return True

test = Solution()
print test.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) # True
print test.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) # False