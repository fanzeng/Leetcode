# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.s = 0
        self.traverse(root)
        return root
        
    def traverse(self, n):
        if n.right is not None:
            self.traverse(n.right)
        v = n.val
        n.val += self.s
        self.s += v
        if n.left is not None:
            self.traverse(n.left)
