class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.d = {}
        i = 0
        for rect in rects:
            for r in xrange(rect[0], rect[2]+1):
                for c in xrange(rect[1], rect[3]+1):
                    self.d[i] = [r, c]
                    i += 1
        # print self.d
        self.total = i-1

    def pick(self):
        """
        :rtype: List[int]
        """
        from random import randint
        return self.d[randint(0, self.total)]

obj = Solution([[1,1,5,5]])
print obj.pick()

obj = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
print obj.pick()
