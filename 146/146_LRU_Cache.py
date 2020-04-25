class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.LRU = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.d.get(key)
        if val is None:
            return -1
        else:
            self.LRU.remove(key)
            self.LRU.append(key)
            return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.d[key] = value
        if key in self.LRU:
            self.LRU.remove(key)
            self.LRU.append(key)
        else:
            if len(self.LRU) == self.capacity:
                self.d[self.LRU.pop(0)] = None
                self.LRU.append(key)
                # print 'after put', key, ', self.LRU =', self.LRU, ', self.d =', self.d
            else:
                self.LRU.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print cache.get(1) # returns 1
cache.put(3, 3) # evicts key 2
print cache.get(2) # returns -1 (not found)
cache.put(4, 4) # evicts key 1
print cache.get(1) # returns -1 (not found)
print cache.get(3) # returns 3
print cache.get(4) # returns 4