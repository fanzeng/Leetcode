# You have a queue of integers, you need to retrieve the first unique integer in the queue.
#
# Implement the FirstUnique class:
#
# FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
# int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
# void add(int value) insert value to the queue.


class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l_unique = []
        self.s = set()
        self.s_removed = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        min_order = len(self.l_unique)
        if len(self.l_unique) > 0:
            return self.l_unique[0]
        else:
            return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.s:
            self.l_unique.append(value)
            self.s.add(value)
        elif value not in self.s_removed:
            self.l_unique.remove(value)
            self.s_removed.add(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)