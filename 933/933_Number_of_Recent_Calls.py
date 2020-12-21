class RecentCounter(object):

    def __init__(self):
        self.l_call = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.l_call.append(t)
        count = 0
        if self.l_call[0] >= t-3000:
            return len(self.l_call)
        last_expired_pos = self.binarySearch(self.l_call, t-3000)
        return len(self.l_call) - 1 - last_expired_pos

    def binarySearch(self, arr, x):
        l = 0
        r = len(arr)-1
        m = (l + r) / 2
        while l < r:
            if arr[m] < x and arr[m+1] >= x:
                return m
            if arr[m] < x:
                l = m
                m = (l+r)/2
            elif arr[m] >= x:
                r = m
                m = (l+r)/2
        return m

# Your RecentCounter object will be instantiated and called as such:
obj_0 = RecentCounter()
print obj_0.ping(1) # 1
print obj_0.ping(100) # 2
print obj_0.ping(3001) # 3
print obj_0.ping(3002) # 3

obj_1 = RecentCounter()
print obj_1.ping(642) # 1
print obj_1.ping(1849) # 2
print obj_1.ping(4921) # 1
print obj_1.ping(5936) # 2
print obj_1.ping(5997) # 3