# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import util.BinaryTree as bt

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetric2(root.left, root.right)

    def isSymmetric2(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val is None and right.val is None:
            return True
        if left.val != right.val:
            return False
        outer = TreeNode(0)
        outer.left = left.left
        outer.right = right.right
        inner = TreeNode(0)
        inner.left = left.right
        inner.right = right.left
        return self.isSymmetric(outer) and self.isSymmetric(inner)

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.isSymmetric(tree.root)

# should return False
test_solution([1, 2])
test_solution([1, 2, 2, 1])
test_solution([1, 2, None, 2, 1])
test_solution([1, 2, 2, 2, None, 2])

# should return True
test_solution([1, 2, 2, 3, 4, 4, 3])
test_solution([])
test_solution([1])
test_solution([1, 2, 2, None, 3, 3, None])
test_solution([1, 2, 2, None, 3, 3])
test_solution([3, 4, 4, 5, None, None, 5, 6,None, None, 6])
test_solution([2,3,3,4,None,None,4,None,5,5,None,None,6,6,None,7,8,8,7,9,0,0,1,1,0,0,9])
test_solution([9,14,14,74,None,None,74,None,12,12,None,63,None,None,63,-8,None,None,-8,-53,None,None,-53,None,-96,-96,None,-65,None,None,-65,98,None,None,98,50,None,None,50,None,91,91,None,41,-30,-30,41,None,86,None,-36,-36,None,86,None,-78,None,9,None,None,9,None,-78,47,None,48,-79,-79,48,None,47,-100,-86,None,47,None,67,67,None,47,None,-86,-100,-28,11,None,56,None,30,None,64,64,None,30,None,56,None,11,-28,43,54,None,-50,44,-58,63,None,None,-43,-43,None,None,63,-58,44,-50,None,54,43])
# Given
# a
# binary
# tree, check
# whether
# it is a
# mirror
# of
# itself(ie, symmetric
# around
# its
# center).
#
# For
# example, this
# binary
# tree[1, 2, 2, 3, 4, 4, 3] is symmetric:
#
# 1
# / \
#     2
# 2
# /  \ / \
#     3
# 4
# 4
# 3
#
# But
# the
# following[1, 2, 2, null, 3, null, 3] is not:
#
# 1
# / \
#     2
# 2
# \ \
#     3
# 3
#
# Note:
# Bonus
# points if you
# could
# solve
# it
# both
# recursively and iteratively.