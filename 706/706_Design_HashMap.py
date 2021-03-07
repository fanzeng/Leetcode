class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = [None]*1000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        result = self.hashMap[self.getHash(key)]
        if result is None:
            self.hashMap[self.getHash(key)] = [(key, value)]
        else:
            for i, (k, v) in enumerate(result):
                if k == key:
                    result[i] = (k, value)
                    return
        self.hashMap[self.getHash(key)].append((key, value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        result = self.hashMap[self.getHash(key)]
        if result is None:
            return -1
        for k, v in result:
            if k == key:
                return v
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        result = self.hashMap[self.getHash(key)]
        if result is not None:
            new_result = [(k, v) for k, v in result if k != key]
            self.hashMap[self.getHash(key)] = new_result

    def getHash(self, key):
        return key % 1000

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print hashMap.get(1) # 1
print hashMap.get(3) # -1
hashMap.put(2, 1)
print hashMap.get(2) # 1
hashMap.remove(2)
print hashMap.get(2) # -1