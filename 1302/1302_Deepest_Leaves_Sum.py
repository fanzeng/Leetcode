# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.lSum = [0]
        self.deepestLeavesSumRecursive(root, 0)
        return self.lSum[-1]

    def deepestLeavesSumRecursive(self, node, depth):
        if node is None:
            return
        if len(self.lSum) < depth+1:
            self.lSum.append(node.val)
        else:
            self.lSum[depth] += node.val
        self.deepestLeavesSumRecursive(node.left, depth+1)
        self.deepestLeavesSumRecursive(node.right, depth+1)

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.deepestLeavesSum(tree.root)

test_solution([1,2,3,4,5,None,6,7,None,None,None,None,8]) # 15
test_solution([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]) # 19

