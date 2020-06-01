# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        n = head
        while n.next is not None:
            if hasattr(n, 'visited'):
                return True
            else:
                n.visited = True
            n = n.next
        return False