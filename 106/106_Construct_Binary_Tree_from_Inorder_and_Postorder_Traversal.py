# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt
TreeNode = bt.TreeNode

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeRecursive(inorder, postorder)

    def buildTreeRecursive(self, inorder, postorder):
        if postorder is None or len(postorder) == 0:
            return None
        root_val = postorder[-1]
        # print 'root_val =', root_val
        root_index = inorder.index(root_val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        left_postorder = postorder[:root_index]
        right_postoder = postorder[root_index:-1]
        # print left_inorder, left_postorder, right_inorder, right_postoder
        left_child = self.buildTreeRecursive(left_inorder, left_postorder)
        right_child = self.buildTreeRecursive(right_inorder, right_postoder)
        return TreeNode(root_val, left_child, right_child)


test = Solution()
t = bt.BinaryTree(test.buildTree([9,3,15,20,7], [9,15,7,20,3]))
print t.tolist()
t = bt.BinaryTree(test.buildTree([], []))
print t.tolist()
t = bt.BinaryTree(test.buildTree([1], [1]))
print t.tolist()