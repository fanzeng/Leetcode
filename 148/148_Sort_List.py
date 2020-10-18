# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        l_val = []
        n = head
        while n is not None:
            l_val.append(n.val)
            n = n.next
        l_val = sorted(l_val)
        new_head = ListNode(l_val[0])
        n = new_head
        for val in l_val[1:]:
            n.next = ListNode(val)
            n = n.next
        return new_head
