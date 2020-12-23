# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.l_val = []
        self.traverse(root)
        return self.create(sorted(self.l_val))

    def traverse(self, node):
        if node is not None:
            self.l_val.append(node.val)
            self.traverse(node.left)
            self.traverse(node.right)

    def create(self, list):
        if len(list) == 0:
            return None
        n = TreeNode(list[0])
        n.right = self.create(list[1:])
        return n