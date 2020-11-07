# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        n = head.next
        count = 1
        prev = head
        while n is not None:
            prev.next = n.next
            n.next = None
            head = self.insert(head, n, count)
            count += 1
            n = head
            for i in xrange(count):
                prev = n
                n = n.next
        return head

    def insert(self, head, n, sorted_count):
        m = head
        prev = None
        count = 0
        while count < sorted_count and m.val <= n.val:
            prev = m
            m = m.next
            count += 1
        if prev is None:
            head = n
        else:
            prev.next = n
        n.next = m
        return head
