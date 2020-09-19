class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        rs = RobotState()
        for instruction in instructions:
            rs = self.followInstruction(rs, instruction)
        return (rs.x == 0 and rs.y == 0) or (rs.heading != 90)

    def followInstruction(self, rs, instruction):
        if instruction == 'L':
            rs.heading += 90
            if rs.heading == 360:
                rs.heading = 0
        if instruction == 'R':
            rs.heading -= 90
            if rs.heading == -90:
                rs.heading = 270
        if instruction == 'G':
            if rs.heading == 0:
                rs.x += 1
            if rs.heading == 90:
                rs.y += 1
            if rs.heading == 180:
                rs.x -= 1
            if rs.heading == 270:
                rs.y -= 1
        return rs

class RobotState(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 90

    def __str__(self):
        return 'x, y, heading =' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.heading)

test = Solution()
print test.isRobotBounded("GGLLGG") # True
print test.isRobotBounded("GG") # False
print test.isRobotBounded("GL") # True