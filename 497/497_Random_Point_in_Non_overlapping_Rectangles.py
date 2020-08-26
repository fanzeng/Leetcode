from random import randint
class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.d = {}
        self.rects = rects
        self.total_area = 0
        self.accu_area = []
        for rect in rects:
            area = (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.total_area += area
            self.accu_area.append(self.total_area)
        # print self.accu_area

    def pickPointFromRect(self, rect, remainder):
        remainder -= 1
        w = rect[2] - rect[0] + 1
        if w == 0:
            row = 0
            col = remainder
        else:
            row = remainder / w
            col = remainder % w
        x = rect[0] + col
        y = rect[1] + row
        return [x, y]

    def pick(self):
        """
        :rtype: List[int]
        """
        rand_num = randint(1, self.total_area)
        rect_id = 0
        while self.accu_area[rect_id] < rand_num:
            rect_id += 1
        remainder = rand_num
        if rect_id > 0:
            remainder = rand_num - self.accu_area[rect_id-1]
        # print rect_id, remainder
        return self.pickPointFromRect(self.rects[rect_id], remainder)

obj = Solution([[1,1,5,5]])
print obj.pick()

obj = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
print obj.pick()
