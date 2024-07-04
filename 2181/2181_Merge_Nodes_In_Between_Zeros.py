# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.doMerge(head)
    
    def doMerge(self, n):
        head = n
        if n.next is None:
            return None
        sum = 0
        n = n.next
        while n.val != 0:
            sum += n.val
            n = n.next
        head.val = sum
        head.next = self.doMerge(n)
        return head
