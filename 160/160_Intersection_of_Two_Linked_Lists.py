# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        na = headA
        nb = headB
        la = []
        lb = []
        while na is not None:
            la.append(na)
            na = na.next
        while nb is not None:
            lb.append(nb)
            nb = nb.next
        i = len(la) - 1
        j = len(lb) - 1
        if la[i] != lb[j]:
            return None
        i -= 1
        j -= 1
        while i >= 0 and j >= 0:
            if la[i] != lb[j]:
                return la[i + 1]
            i -= 1
            j -= 1
        return la[i+1]