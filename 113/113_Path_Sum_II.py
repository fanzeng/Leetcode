# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.BinaryTree as bt

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return []
        root.sum = root.val
        root.path = [root.val]
        self.sumFromRootWithPath(root)
        self.l_paths = []
        self.isValInLeaf(root, sum)
        return self.l_paths

    def sumFromRootWithPath(self, root):
        if root is None or root.val is None:
            return
        if root.left is not None:
            root.left.sum = root.sum + root.left.val
            root.left.path = root.path[:]
            root.left.path.append(root.left.val)
            self.sumFromRootWithPath(root.left)

        if root.right is not None:
            root.right.sum = root.sum + root.right.val
            root.right.path = root.path[:]
            root.right.path.append(root.right.val)
            self.sumFromRootWithPath(root.right)

    def isLeaf(self, node):
        return node is not None and node.left is None and node.right is None

    def isValInLeaf(self, root, val):
        if root is None or root.val is None:
            return
        elif self.isLeaf(root):
            if root.sum == val:
                self.l_paths.append(root.path)
        else:
            self.isValInLeaf(root.left, val)
            self.isValInLeaf(root.right, val)


def test_solution(l, sum):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.pathSum(tree.root, sum)

test_solution([5,4,8,11,None,13,4,7,2,None,None,5,1], 22)

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
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
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]