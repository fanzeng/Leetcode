# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import util.BinaryTree as bt

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_height = self.height(root.left) + int(root.left is not None)
        right_height = self.height(root.right) + int(root.right is not None)
        if abs(left_height - right_height) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def height(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.isBalanced(tree.root)

test_solution([3,9,20,None,None,15,7])
test_solution([1,2,2,3,3,None,None,4,4])
test_solution([1,None,2,None,3])

# Given
# a
# binary
# tree, determine if it is height - balanced.
#
# For
# this
# problem, a
# height - balanced
# binary
# tree is defined as:
#
# a
# binary
# tree in which
# the
# left and right
# subtrees
# of
# every
# node
# differ in height
# by
# no
# more
# than
# 1.
#
# Example
# 1:
#
# Given
# the
# following
# tree[3, 9, 20, null, null, 15, 7]:
#
# 3
# / \
#     9
# 20
# / \
#     15
# 7
# Return
# true.
#
# Example
# 2:
#
# Given
# the
# following
# tree[1, 2, 2, 3, 3, null, null, 4, 4]:
#
# 1
# / \
#     2
# 2
# / \
#     3
# 3
# / \
#     4
# 4
# Return
# false.