# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        node = self
        res = ""
        while node.next != None:
            res += "{}->".format(node.val)
            node = node.next
        res += "{}".format(node.val)
        return res

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        cursor1 = ListNode(0)
        cursor2 = ListNode(0)
        head = res
        cursor1.next = l1
        cursor2.next = l2
        carry = 0
        ending = False
        while not ending:

            if cursor1.next != None:
                cursor1 = cursor1.next
            else:
                cursor1.val = 0
            if cursor2.next != None:
                cursor2 = cursor2.next
            else:
                cursor2.val = 0
            sum = cursor1.val + cursor2.val + carry
            ending = (cursor1.next == None and cursor2.next == None)
            if sum >= 10:
                sum -= 10
                carry = 1
                if ending:
                    res.next = ListNode(sum)
                    res = res.next
                    res.next = ListNode(carry)
                    res = res.next
                    break
            else:
                carry = 0
            res.next = ListNode(sum)
            res = res.next

        return head.next

def main():
    l1 = ListNode(5)
    l1.next = ListNode(4)
    l1.next.next =ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next =ListNode(4)

    l3 = ListNode(5)
    l3.next = ListNode(6)
    l3.next.next =ListNode(4)
    l3.next.next.next =ListNode(2)

    test = Solution()

    print l1
    print l2
    print l3
    print test.addTwoNumbers(l1, l2)
    print test.addTwoNumbers(l1, l3)

main()