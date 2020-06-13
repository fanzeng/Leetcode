class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.arr = sorted(nums, reverse=True)[:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if (len(self.arr)) < self.k:
            i = len(self.arr)-1
            while i >= 0:
                if val > self.arr[i]:
                    i -= 1
                else:
                    break
            self.arr = self.arr[:i+1] + [val] + self.arr[i+1:]
            return self.arr[-1]

        if val <= self.arr[-1]:
            return self.arr[-1]

        length = len(self.arr)
        l = 0
        r = length-1
        m = (l + r)/2
        while True:
            if val == self.arr[m]:
                break
            elif val > self.arr[m]:
                r = m
            else:
                l = m
            if r - l <= 1:
                if self.arr[l] <= val:
                    m = l
                else:
                    m = r
                break
            else:
                m = (l + r) / 2
        # print l, m ,r, self.arr
        self.arr = self.arr[:m] + [val] + self.arr[m:-1]
        # print self.arr
        return self.arr[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(3, arr)
print kthLargest.add(3) # returns 4
print kthLargest.add(5) # returns 5
print kthLargest.add(10) # returns 5
print kthLargest.add(9) # returns 8
print kthLargest.add(4) # returns 8