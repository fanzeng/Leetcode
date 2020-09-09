# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.l_number = []
        self.getNumber(root, '')
        return sum([int(s, 2) for s in self.l_number])

    def getNumber(self, node, prefix):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.l_number.append(prefix + str(node.val))
        else:
            prefix += str(node.val)
            self.getNumber(node.left, prefix)
            self.getNumber(node.right, prefix)