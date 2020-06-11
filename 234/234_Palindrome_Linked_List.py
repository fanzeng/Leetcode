# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.isListTheSame(head, self.reverseList(head, None))

    def isListTheSame(self, a, b):
        if a is None and b is None:
            return True
        if (a is not None and b is None) or (a is None and b is not None):
            return False
        else:
            return a.val == b.val and self.isListTheSame(a.next, b.next)

    def reverseList(self, head, rest):
        if head is None:
            return rest
        n = ListNode(head.val)
        n.next = rest
        return self.reverseList(head.next, n)
