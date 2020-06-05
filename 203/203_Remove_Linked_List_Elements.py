# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        n = head
        while n.val == val:
            if n.next is not None:
                n = n.next
            else:
                break
        if n.val == val:
            return None
        else:
            head = n
            prev = n

        while n.next is not None:
            n = n.next
            if n.val != val:
                prev.next = n
                prev = n

        if n.val == val:
            prev.next = None

        return head

head = ListNode(1)
n = head
for i in xrange(2, 7):
    n.next = ListNode(i)
    n = n.next

test = Solution()
test.removeElements(head, 6)