# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        self.insertIntoBSTRecursive(root, val)
        return root

    def insertIntoBSTRecursive(self, node, val):
        if val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.insertIntoBSTRecursive(node.right, val)
        else:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insertIntoBSTRecursive(node.left, val)
