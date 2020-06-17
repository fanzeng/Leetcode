class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q = [x] + self.q

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0

obj = MyStack()
print obj.push(1)
print obj.push(2)
print obj.top() # 2
print obj.pop() # 2
print obj.empty() # False