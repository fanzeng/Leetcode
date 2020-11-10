# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val, max_val, max_diff = self.traverse(root)
        print 'min_val, max_val, max_diff =', min_val, max_val, max_diff
        return max_diff

    def traverse(self, node):
        if node is None:
            return None, None, 0
        min_left, max_left, diff_left = self.traverse(node.left)
        min_right, max_right, diff_right = self.traverse(node.right)
        min_no_none = [x for x in [min_left, min_right] if x is not None]
        max_no_none = [x for x in [max_left, max_right] if x is not None]
        min_desc = min(min_no_none) if len(min_no_none) > 0 else None
        max_desc = max(max_no_none) if len(max_no_none) > 0 else None
        diff = max(abs(node.val - min_desc) if min_desc is not None else 0, abs(node.val - max_desc) if max_desc is not None else 0)
        return node.val if min_desc is None else min(node.val, min_desc), node.val if max_desc is None else max(node.val, max_desc), max(diff_left, diff_right, diff)