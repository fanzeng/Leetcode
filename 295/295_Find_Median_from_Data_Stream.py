class MedianFinder(object):

    def __init__(self):
        self.arr = []        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.arr) == 0:
            self.arr = [num]
            return
        if num <= self.arr[0]:
            self.arr = [num] + self.arr
            return
        l = 0
        r = len(self.arr) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if self.arr[mid] == num:
                break
            elif self.arr[mid] < num:
                l = mid
            else:
                r = mid
        i = l
        while i < r:
            if self.arr[i] <= num and self.arr[i+1] > num:
                break
            i += 1
        self.arr = self.arr[:i+1] + [num] + self.arr[i+1:]

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.arr) % 2 == 1:
            return self.arr[len(self.arr)/2]
        else:
            return (self.arr[len(self.arr)/2-1] + self.arr[len(self.arr)/2])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
