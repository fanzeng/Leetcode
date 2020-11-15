# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.listToNum(l1)
        n2 = self.listToNum(l2)
        return self.numToList(n1 + n2)

    def listToNum(self, head):
        num = head.val
        n = head.next
        while n is not None:
            num *= 10
            num += n.val
            n = n.next
        return num

    def numToList(self, n):
        # print 'n =', n
        if n == 0:
            return ListNode(0)
        if n == 1:
            return ListNode(1)
        b = 1
        while b <= n:
            b *= 10
        b /= 10
        l_bit = []
        while True:
            bit = n / b
            l_bit.append(bit)
            n %= b
            b /= 10
            if b < 1:
                break
        head = ListNode(l_bit[0])
        n = head
        for bit in l_bit[1:]:
            n.next = ListNode(bit)
            n = n.next
        return head
