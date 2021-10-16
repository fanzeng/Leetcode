# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = self.getLength(head)
        if length < k:
            part_length_large = 1
            num_large = length
            num_small = k - length
        else:

            if length % k == 0:
                part_length_large = length / k
                num_large = k
                num_small = 0
            else:
                part_length_large = length / k + 1
                diff = part_length_large * k - length
                num_small = diff
                num_large = k - diff
        return self.split(head, num_large, num_small, part_length_large)

    def split(self, head, num_large, num_small, part_length_large):
        n = head
        m = n
        prev = n
        res = []
        for i in xrange(num_large):
            part_head = m
            res.append(part_head)
            for j in xrange(part_length_large):
                prev = n
                n = n.next
            m = n
            prev.next = None
        for i in xrange(num_small):
            part_head = m
            if m is None:
                res.append(None)
                continue
            res.append(part_head)
            for j in xrange(part_length_large-1):
                prev = n
                n = n.next
            m = n
            prev.next = None
        return res

    def getLength(self, head):
        n = head
        count = 0
        while n:
            count += 1
            n = n.next
        return count