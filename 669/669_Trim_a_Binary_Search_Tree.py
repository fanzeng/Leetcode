# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        self.low = low
        self.high = high
        return self.trimNode(root)

    def trimNode(self, node):
        if node is None:
            return None
        if node.val < self.low:
            # the whole left subtree must be below low too and can be trimmed altogether
            return self.trimNode(node.right)
        if node.val > self.high:
            return self.trimNode(node.left)
        else:
            node.left = self.trimNode(node.left)
            node.right = self.trimNode(node.right)
            return node

def test_solution(l, low, high):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    root = test.trimBST(tree.root, low, high)
    print bt.BinaryTree(root).tolist()

test_solution([1,0,2], 1, 2) # [1,None,2]
test_solution([3,0,4,None,2,None,None,1], 1, 3) # [3,2,None,1]
test_solution([1], 1, 2) # [1]
test_solution([1,None,2], 1, 3) # [1,None,2]
test_solution([1,None,2], 2, 4) # [2]
