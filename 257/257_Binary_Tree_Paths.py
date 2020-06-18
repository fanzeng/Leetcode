# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.getPaths(root, '')
        return self.res

    def getPaths(self, n, s):
        if n is not None:
            if len(s) > 0:
                s += '->'
            s += str(n.val)
            if n.left is not None:
                self.getPaths(n.left, s)
            if n.right is not None:
                self.getPaths(n.right, s)
            if n.left is None and n.right is None:
                self.res.append(s)