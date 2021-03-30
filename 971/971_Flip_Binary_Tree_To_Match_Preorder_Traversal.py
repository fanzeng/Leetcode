# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        return self.flipMatchVoyageRecursive(root, voyage, [])

    def flipMatchVoyageRecursive(self, node, voyage, flipped):
        if node is None:
            if len(voyage) == 0:
                return flipped
            else:
                return [-1]
        if len(voyage) == 0:
            return [-1]
        if voyage[0] != node.val:
            return [-1]
        preorder = self.preorder(node)
        # print 'preorder =', preorder
        if preorder == voyage:
            return flipped
        else:
            preorder_left = self.preorder(node.left)
            voyage = voyage[1:]
            voyage_0 = voyage[:len(preorder_left)]
            voyage_1 = voyage[len(preorder_left):]
            # print 'voyage_0 =', voyage_0, 'voyage_1 =', voyage_1
            flipped_left = self.flipMatchVoyageRecursive(node.left, voyage_0, flipped)
            flipped_right = self.flipMatchVoyageRecursive(node.right, voyage_1, flipped)
            if flipped_left != [-1] and flipped_right != [-1]:
                return flipped_left + flipped_right
            voyage_0 = voyage[:len(voyage) - len(preorder_left)]
            voyage_1 = voyage[len(voyage) - len(preorder_left):]
            flipped_left = self.flipMatchVoyageRecursive(node.left, voyage_1, flipped)
            flipped_right = self.flipMatchVoyageRecursive(node.right, voyage_0, flipped)
            if flipped_left != [-1] and flipped_right != [-1]:
                return [node.val] + flipped_left + flipped_right
            return [-1]

    def preorder(self, node):
        if node is None:
            return []
        return [node.val] + self.preorder(node.left) + self.preorder(node.right)

def test_solution(l, voyage):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.flipMatchVoyage(tree.root, voyage)

test_solution([1,2], [2,1]) # [-1]
test_solution([1,2,3], [1,3,2]) # [1]
test_solution([1,2,3], [1,2,3]) # []
test_solution([5,1,2,None,None,4,3], [5,2,3,4,1]) # [5,2]