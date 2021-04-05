class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.arr = [None]*k
        self.pFront = 0
        self.pRear = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.arr[self.pRear] is not None:
            return False
        self.arr[self.pRear] = value
        self.pRear += 1
        if self.pRear == self.k:
            self.pRear = 0
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.arr[self.pFront] is None:
            return False
        self.arr[self.pFront] = None
        self.pFront += 1
        if self.pFront == self.k:
            self.pFront = 0
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.arr[self.pFront] is None:
            return -1
        return self.arr[self.pFront]

    def Rear(self):
        """
        :rtype: int
        """
        if self.arr[self.pRear-1] is None:
            return -1
        return self.arr[self.pRear-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.arr[self.pFront] is None

    def isFull(self):
        """
        :rtype: bool
        """
        return self.arr[self.pRear] is not None

myCircularQueue = MyCircularQueue(3)
print myCircularQueue.enQueue(1) # True
print myCircularQueue.enQueue(2) # True
print myCircularQueue.enQueue(3) # True
print myCircularQueue.enQueue(4) # False
print myCircularQueue.Rear() # 3
print myCircularQueue.isFull() # True
print myCircularQueue.deQueue() # True
print myCircularQueue.enQueue(4) # True
print myCircularQueue.Rear() # 4