# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.low = low
        self.high = high
        return self.rangeSum(root)

    def rangeSum(self, node):
        if node is None:
            return 0
        sum = 0
        if node.val >= self.low and node.val <= self.high:
            sum = node.val
        return sum + self.rangeSum(node.left) + self.rangeSum(node.right)