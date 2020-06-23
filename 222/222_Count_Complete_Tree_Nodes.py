# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countNodesRecursive(root)

    def countNodesRecursive(self, node):
        if node is None:
            return 0
        left_count = 0
        right_count = 0
        if node.left is not None:
            left_count = self.countNodesRecursive(node.left)
        if node.right is not None:
            right_count = self.countNodesRecursive(node.right)
        return 1 + left_count + right_count
