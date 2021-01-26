# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head is None:
            return None

        length = 0
        node = head
        tail = head
        while node is not None:
            length += 1
            tail = node
            node = node.next
        if length == 1 or k % length == 0:
            return head
        orig_head = head
        node = head
        shift_left = length-(k % length)
        for i in xrange(shift_left-1):
            node = node.next
        new_head = node.next
        node.next = None
        tail.next = orig_head
        return new_head

        