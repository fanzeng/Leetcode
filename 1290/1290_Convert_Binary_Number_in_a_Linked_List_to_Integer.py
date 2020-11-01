# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if head is None:
            return None
        n = head
        li = []
        while n is not None:
            li.append(str(n.val))
            n = n.next
        if len(li) == 0:
            return None
        return int(''.join(li), 2)