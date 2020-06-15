from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.d.get(val) is not None:
            return False
        else:
            self.d[val] = True
            self.size += 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.d.get(val) is None:
            return False
        else:
            self.d.pop(val)
            self.size -= 1
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.d.keys()[randint(0, self.size-1)]


obj = RandomizedSet()
print obj.insert(1) # True
print obj.remove(2) # False
print obj.insert(2) # True
print obj.getRandom() # 1 or 2 randomly
print obj.remove(1) # True
print obj.insert(2) # False
print obj.getRandom() # 2