"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.d_parent = {}
        self.genDictParent(root, None, False)
        self.connectRecursive(root)
        return root

    def genDictParent(self, node, parent, is_left):
        if node is None:
            return
        self.d_parent[node] = (parent, is_left)
        self.genDictParent(node.left, node, True)
        self.genDictParent(node.right, node, False)

    def connectRecursive(self, n):
        if n is None:
            return
        self.populate(n)
        self.connectRecursive(n.left)
        self.connectRecursive(n.right)

    def populate(self, n):
        if n is None:
            return
        parent, is_left = self.d_parent[n]
        if is_left:
            n.next = parent.right
        elif parent is not None and parent.next is not None:
            n.next = parent.next.left


