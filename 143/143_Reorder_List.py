# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        l_node = []
        n = head
        while True:
            l_node.append(n)
            if n.next is None:
                break
            n = n.next

        n = head
        i = 0
        while (i >= 0 and i < len(l_node)/2) or (i < 0 and -i <= len(l_node)/2):
            print i, n.val
            if i >= 0:
                i += 1
            i *= -1
            n.next = l_node[i]
            n = n.next
        n.next = None