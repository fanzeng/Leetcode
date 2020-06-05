# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        n = head
        l = []
        while n is not None:
            l.append(n.val)
            n = n.next
        res = ListNode(l[-1])
        n = res
        for v in l[-2::-1]:
            n.next = ListNode(v)
            n = n.next
        n.next = None
        return res

