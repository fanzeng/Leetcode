from random import randint
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.partial_sum = []
        s = 0
        for x in w:
            s += x
            self.partial_sum.append(s)
        self.sum_w = self.partial_sum[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        r = randint(1, self.sum_w)
        for i in xrange(len(self.w)-1, -1, -1):
            if r > self.partial_sum[i-1]:
                return i
        return 0
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

def test_solution(case):
    test = Solution(case)
    d = {}
    for x in xrange(len(test.w)):
        d[x] = 0
    for i in xrange(10000):
        d[test.pickIndex()] += 1
    print d

print test_solution([1])
print test_solution([1, 3])
print test_solution([1, 2, 3])
print test_solution([1, 2, 3, 4])


