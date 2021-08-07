"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.d = {}
        self.traverse(root, 0)
        height = max(self.d.keys())
        return [self.d[depth] for depth in xrange(height+1)]

    def traverse(self, n, depth):
        if n is None:
            return
        if self.d.get(depth):
            self.d[depth].append(n.val)
        else:
            self.d[depth] = [n.val]
        for child in n.children:
            self.traverse(child, depth+1)