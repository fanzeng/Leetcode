# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        self.sumFromNode(root)
        return self.sumAllNodes(root)

    # calculate how many paths starting from a given node
    def sumFromNode(self, node):
        if node is None or node.val is None:
            return
        node.count = int(node.val == self.sum)
        if node.left is not None:
            node.count += self.sumFromNodeRecursive(node.left, node.val)
            self.sumFromNode(node.left)
        if node.right is not None:
            node.count += self.sumFromNodeRecursive(node.right, node.val)
            self.sumFromNode(node.right)

    # given a node and a partial sum, calculate how many paths sum to self.sum
    def sumFromNodeRecursive(self, node, part_sum):
        if node is None or node.val is None:
            return 0
        count = int(part_sum + node.val == self.sum)
        if node.left is not None:
            count += self.sumFromNodeRecursive(node.left, part_sum + node.val)
        if node.right is not None:
            count += self.sumFromNodeRecursive(node.right, part_sum + node.val)
        return count

    def sumAllNodes(self, node):
        if node is None or node.val is None:
            return 0
        count = node.count
        if node.left is not None:
            count += self.sumAllNodes(node.left)
        if node.right is not None:
            count += self.sumAllNodes(node.right)
        return count

def test_solution(l, sum):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.pathSum(tree.root, sum)

test_solution([10,5,-3,3,2,None,11,3,-2,None,1], 8) # 3