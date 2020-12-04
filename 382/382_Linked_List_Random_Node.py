# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        n = head
        self.l_val = []
        while n is not None:
            self.l_val.append(n.val)
            n = n.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        index = random.randint(0, len(self.l_val)-1)
        return self.l_val[index]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()