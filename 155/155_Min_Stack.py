class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.l) == 0 or x < self.min:
            self.min = x
        self.l = [x] + self.l

    def pop(self):
        """
        :rtype: None
        """
        if len(self.l) > 0:
            x = self.l[0]
            if len(self.l) > 1:
                self.l = self.l[1:]
            else:
                self.l = []
        else:
            x = None
        if self.min == x:
            if len(self.l) == 0:
                self.min = None
            else:
                self.min = min(self.l)
        return x

    def top(self):
        """
        :rtype: int
        """
        if len(self.l) > 0:
            return self.l[0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print param_3
print param_4