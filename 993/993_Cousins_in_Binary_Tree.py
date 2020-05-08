# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False
        px = self.getParent(root, x)
        py = self.getParent(root, y)
        dx = self.getDepth(root, x, 0)
        dy = self.getDepth(root, y, 0)
        # print px, py, dx, dy
        return dx is not None and dy is not None and dx == dy and px is not None and py is not None and px != py

    def getParent(self, root, x):
        if root.left is not None:
            if root.left.val == x:
                return root
            else:
                res_left = self.getParent(root.left, x)
                if res_left is not None:
                    return res_left
        if root.right is not None:
            if root.right.val == x:
                return root
            else:
                res_right = self.getParent(root.right, x)
                if res_right is not None:
                    return res_right
        else:
            return None

    def getDepth(self, root, x, curDepth):
        if root is None:
            return None
        if root.val == x:
            return curDepth
        res_left = self.getDepth(root.left, x, curDepth + 1)
        if res_left is not None:
            return res_left
        res_right = self.getDepth(root.right, x, curDepth + 1)
        if res_right is not None:
            return res_right
        return None