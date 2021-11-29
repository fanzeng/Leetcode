"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        return self.flattenRecursive(head, None)

    def flattenRecursive(self, n, rest):
        if n is None:
            return rest
        if n.child is None:
            if n.next is None:
                n.next = rest
                if rest is not None:
                    rest.prev = n
                return n
            else:
                n.next = self.flattenRecursive(n.next, rest)
                n.next.prev = n
                return n
        else:
            child = n.child
            n.child = None
            child.prev = n
            n.next = self.flattenRecursive(child, self.flattenRecursive(n.next, rest))
        return n