# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.BinaryTree as bt

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sumFromRoot(root)
        return self.isValInLeaf(root, sum)


    def sumFromRoot(self, root):
        if root is None or root.val is None:
            return
        if root.left is not None:
            root.left.val += root.val
            self.sumFromRoot(root.left)

        if root.right is not None:
            root.right.val += root.val
            self.sumFromRoot(root.right)

    def isLeaf(self, node):
        return node is not None and node.left is None and node.right is None

    def isValInLeaf(self, root, val):
        if root is None or root.val is None:
            return False
        elif self.isLeaf(root):
            if root.val == val:
                return True
            else:
                return False
        else:
            return self.isValInLeaf(root.left, val) or self.isValInLeaf(root.right, val)


def test_solution(l, sum):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.hasPathSum(tree.root, sum)

test_solution([5,4,8,11,None,13,4,7,2,None,None,None,1], 22)
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.