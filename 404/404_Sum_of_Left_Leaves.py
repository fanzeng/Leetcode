# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumOfLeftLeavesRecursive(root, False)

    def sumOfLeftLeavesRecursive(self, node, is_left):
        if node is None:
            return 0
        else:
            if is_left and node.left is None and node.right is None:
                sum = node.val
            else:
                sum = 0
            sum += self.sumOfLeftLeavesRecursive(node.left, True)
            sum += self.sumOfLeftLeavesRecursive(node.right, False)
        return sum