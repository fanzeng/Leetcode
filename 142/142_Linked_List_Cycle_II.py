# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = head
        d = {}
        while n is not None:

            if d.get(n.val) is None:
                d[n.val] = [n]
            else:
                if n in d[n.val]:
                    return n
                else:
                    d[n.val].append(n)
            n = n.next