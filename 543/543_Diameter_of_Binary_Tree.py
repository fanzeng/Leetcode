# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import util.BinaryTree as bt

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        diameter_l = self.diameterOfBinaryTree(root.left)
        diameter_r = self.diameterOfBinaryTree(root.right)
        height_l = self.height(root.left)
        height_r = self.height(root.right)
        diameter_via_root = height_l + height_r + int(root.left is not None) + int(root.right is not None)
        # print root.val, diameter_l, diameter_r, height_l,height_r, diameter_via_root
        return max(diameter_via_root, max(diameter_l, diameter_r))

    def height(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.diameterOfBinaryTree(tree.root)

test_solution([1, 2, 3, 4, 5])
