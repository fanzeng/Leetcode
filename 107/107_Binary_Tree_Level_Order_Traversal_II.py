# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.BinaryTree as bt

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        l = []
        depth = 0
        q = [(root, depth)]
        while len(q) > 0:
            n, depth = q.pop(0)
            l.append((n.val, depth))
            if n.left is not None:
                q.append((n.left, depth+1))
            if n.right is not None:
                q.append((n.right, depth+1))
        res = []
        for d in xrange(depth, -1, -1):
            level = [x[0] for x in l if x[1] == d]
            res.append(level)
        return res

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.levelOrderBottom(tree.root)

test_solution([3,9,20,None,None,15,7])
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]