class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort by ascending end points
        # burst the balloons starting from the smallest end points
        # reasoning:
        # for each interval in points (the argument to this function),
        # we have to burst it with an arrow between its start and end points.
        # say we prefer to choose these terminal points, then for any interval,
        # the only reason that forces us to choose
        # an internal point other than the terminals,
        # is that the internal point is a terminal point of another interval.
        # it follows that we only need to consider all terminal points.
        # in other words, if there is a best
        # solution where there are internal points picked as arrow positions,
        # we will be able to move these internal arrow positions to nearby terminal points
        # without changing the effects, and as a result arrive at an equivalent solution
        # by only considering the terminal points.
        # using similar logic,
        # say we prefer end points over start points,
        # the only reason that forces us to choose the start point over the end point for some interval A,
        # is for some interval B, the start point sits in B but the end point does not,
        # thus by taking the start point of interval A we can burst more balloons at the same time.
        # but the same effect can be achieved by taking the end point of interval B,
        # since the end point of interval B will be sitting in interval A.
        # therefore we only need to consider arrows launched from a subset of all end points,
        # and if we find the best solution for the problem where we are restricted to launch from end points,
        # the solution will be equivalent to the best solution to the original problem.
        # sort the intervals by ascending end points.
        # Then consider the first interval, it has to be burst no matter how,
        # but since no other end point can launch an arrow to burst it,
        # we have to launch an arrow here to burst it.
        # same argument applies recursively afterwards.
        return self.findMinArrowShotsRecursive(sorted(points, key=lambda x:x[1]))

    def findMinArrowShotsRecursive(self, points):
        if len(points) < 2:
            return len(points)
        remain = self.burst(points[0][1], points)
        return 1 + self.findMinArrowShotsRecursive(remain)

    def isArrowAbleToBurst(self, arrow, point):
        return point[0] <= arrow and arrow <= point[1]

    def burst(self, arrow, points):
        remain = points[:]
        for p in points:
            if p[0] > arrow:
                break
            if self.isArrowAbleToBurst(arrow, p):
                remain.remove(p)
        return remain

test = Solution()
print test.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) # 2
print test.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) # 4
print test.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) # 2
print test.findMinArrowShots([[1,2]]) # 1
print test.findMinArrowShots([[2,3],[2,3]]) # 1
print test.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]) # 2
print test.findMinArrowShots([[1,9],[7,16],[2,5],[7,12],[9,11],[2,10],[9,16],[3,9],[1,3]]) # 2
print test.findMinArrowShots(
    [[11702305,96123230],[37477084,64813411],[72660336,131786841],
     [5750846,38372575],[661313,34587170],[41616124,125970019],
     [39819582,40920127],[98898814,147132181],[10515434,96505798],[74344043,134657793]]
) # 3
print test.findMinArrowShots(
    [[4289383,51220269],[81692777,96329692],[57747793,81986128],
     [19885386,69645878],[96516649,186158070],[25202362,75692389],
     [83368690,85888749],[44897763,112411689],[65180540,105563966],[4089172,7544908]]
) # 4