# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.BinaryTree as bt

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.maxSumOfOneBranch(root)
        return self.maxSumOfTwoBranch(root)


    def maxSumOfOneBranch(self, root):
        if root is None or root.val is None:
            return None
        root.maxSum1 = None
        leftMaxSum1 = None
        rightMaxSum1 = None
        if root.left is not None:
            root.left.maxSum1 = self.maxSumOfOneBranch(root.left)
            leftMaxSum1 = root.left.maxSum1
        if root.right is not None:
            root.right.maxSum1 = self.maxSumOfOneBranch(root.right)
            rightMaxSum1 = root.right.maxSum1
        if root.left is None and root.right is None:
            root.maxSum1 = root.val
        else:
            root.maxSum1 = max(root.val, max(leftMaxSum1, rightMaxSum1) + root.val)
        return root.maxSum1

    def maxSumOfTwoBranch(self, root):
        if root is None or root.val is None:
            return None
        leftMaxSum2 = None
        rightMaxSum2 = None
        if root.left is not None:
            root.left.maxSum2 = self.maxSumOfTwoBranch(root.left)
            leftMaxSum2 = root.left.maxSum2
        if root.right is not None:
            root.right.maxSum2 = self.maxSumOfTwoBranch(root.right)
            rightMaxSum2 = root.right.maxSum2
        root.maxSum2 = root.val
        if root.left is not None and root.left.maxSum1 is not None and root.left.maxSum1 > 0:
            root.maxSum2 += root.left.maxSum1
        if root.right is not None and root.right.maxSum1 is not None and root.right.maxSum1 > 0:
            root.maxSum2 += root.right.maxSum1
        root.maxSum2 = max(max(leftMaxSum2, rightMaxSum2), root.maxSum2)
        return root.maxSum2

def test_solution(l, sum):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.maxPathSum(tree.root)

test_solution( [1,2,3], 6)
test_solution([-10,9,20,None,None,15,7], 42)
