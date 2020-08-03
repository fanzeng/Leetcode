class MyHashSet(object):
    # according the problem requirement, built-in data structure of set and dict are not used.
    # list is used to simulate an array.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = [None]*1000

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.hash(key)
        if self.l[h] is None:
            self.l[h] = [key]
        elif key not in self.l[h]:
            self.l[h].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.hash(key)
        if self.l[h] is not None and key in self.l[h]:
            self.l[h].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = self.hash(key)
        if self.l[h] is not None:
            return key in self.l[h]
        else:
            return False

    def hash(self, key):
        return key % 1000

obj = MyHashSet()
obj.add(1)
obj.add(2)
print obj.contains(1) # returns true
print obj.contains(3) # returns false (not found)
obj.add(2)
print obj.contains(2) # returns true
obj.remove(2)
print obj.contains(2) # returns false (already removed)