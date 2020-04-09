# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        s = str(self.val)
        if self.next is not None:
            s +=  '->' + str(self.next)
        return s

class List(object):
    def __init__(self, l):
        if l is not None:
            if len(l) > 0:
                self.head = ListNode(l[0])
                i = 1
                n = self.head
                while i < len(l):
                    n.next = ListNode(l[i])
                    i += 1
                    n = n.next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 1
        n = head
        l = [head]
        while n.next is not None:
            n = n.next
            l.append(n)
            count += 1
        return l[count/2]

test = Solution()
print test.middleNode(List([1,2,3,4,5]).head)
print test.middleNode(List([1,2,3,4,5,6]).head)