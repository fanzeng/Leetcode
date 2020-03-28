# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is not None:
            return str(self.val) + '->' + str(self.next)
        else:
            return str(self.val)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = head
        if n is None:
            return n
        outhead = ListNode(n.val)
        out = outhead
        s = {n.val}
        while n is not None:
            if n.val not in s:
                next = ListNode(n.val)
                out.next = next
                out = out.next
                s.add(n.val)
            if n.next is None:
                break
            else:
                n = n.next
        return outhead

def createList(arr):
    if len(arr) < 1:
        return None
    n = ListNode(arr[0])
    if len(arr) == 1:
        return n
    n.next = createList(arr[1:])
    return n

test = Solution()
l = None
print 'l=', l
print 'test.deleteDuplicates(l) =', test.deleteDuplicates(l)

l = createList([1, 1, 2])
print 'l =', l
print 'test.deleteDuplicates(l) =', test.deleteDuplicates(l)

l = createList([1, 1, 2, 3, 3])
print 'l =', l
print 'test.deleteDuplicates(l) =', test.deleteDuplicates(l)

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3