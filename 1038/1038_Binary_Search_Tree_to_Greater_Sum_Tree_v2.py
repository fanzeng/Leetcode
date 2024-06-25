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
        self.traverse(root, 0)
        return root
        
    def traverse(self, n, s):
        n.val += s
        if n.right is not None:
            n.val += self.sumSubTree(n.right)
            self.traverse(n.right, s)
        if n.left is not None:
           self.traverse(n.left, n.val)
    
    def sumSubTree(self, node):
        s = node.val
        if node.right is not None:
            s += self.sumSubTree(node.right)
        if node.left is not None:
            s += self.sumSubTree(node.left)
        return s
