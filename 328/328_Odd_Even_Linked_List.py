# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        odd_head = head
        even_head = head.next
        odd_n = odd_head
        even_n = even_head
        n = even_head.next
        count = 3
        while n is not None:
            if count % 2 == 1:
                odd_n.next = n
                odd_n = odd_n.next
            else:
                even_n.next = n
                even_n = even_n.next
            n = n.next
            count += 1
        odd_n.next = even_head
        even_n.next = None
        return odd_head

