# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.lists = lists
        head = ListNode(0)
        p = head
        while not self.over():
            m = 10000  # -10^4 <= lists[i][j] <= 10^4
            argmin = -1
            for i, li in enumerate(self.lists):
                if li is not None and li.val < m:
                    m = li.val
                    argmin = i
            p.next = ListNode(m)
            p = p.next
            self.lists[argmin] = self.lists[argmin].next
        return head.next

    def over(self):
        for i, li in enumerate(self.lists):
            if li is not None:
                return False
        return True