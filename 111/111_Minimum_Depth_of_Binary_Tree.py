# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.BinaryTree as bt

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        root.depth = 1
        q = [root]
        while len(q) > 0:
            n = q.pop(0)
            if n.left is None and n.right is None:
                return n.depth
            else:
                if n.left is not None:
                    n.left.depth = n.depth + 1
                    q.append(n.left)
                if n.right is not None:
                    n.right.depth = n.depth + 1
                    q.append(n.right)



def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.minDepth(tree.root)

test_solution([3,9,20,None,None,15,7])
test_solution([3,9,20,15,7])
test_solution([])
test_solution([0])
test_solution([1,None,2,None,3])

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.