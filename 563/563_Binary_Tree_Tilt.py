# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum_val, sum_tilt = self.findTiltRecursive(root)
        return sum_tilt

    def findTiltRecursive(self, node):
        if node is None:
            return 0, 0
        sum_val_left, sum_tilt_left = self.findTiltRecursive(node.left)
        sum_val_right, sum_tilt_right = self.findTiltRecursive(node.right)
        sum_val = sum_val_left + sum_val_right + node.val
        sum_tilt = sum_tilt_left + sum_tilt_right + abs(sum_val_left - sum_val_right)
        return sum_val, sum_tilt