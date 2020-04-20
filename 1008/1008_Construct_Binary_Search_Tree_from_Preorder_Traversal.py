# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.BinaryTree as bt
from util.BinaryTree import TreeNode

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None or len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            self.addNode(root, i)
        return root

    def addNode(self, root, i):
        n = root
        if i < n.val:
            if n.left is None:
                n.left = TreeNode(i)
            else:
                self.addNode(n.left, i)
        if i > n.val:
            if n.right is None:
                n.right = TreeNode(i)
            else:
                self.addNode(n.right, i)
        # i == n.val is not possible, since
        # there is the guarantee that the values of preorder are distinct.


test = Solution()
root = test.bstFromPreorder([8,5,1,7,10,12]) # [8,5,10,1,7,null,12]
print root.val, root.left.val
print bt.BinaryTree(root).tolist()
