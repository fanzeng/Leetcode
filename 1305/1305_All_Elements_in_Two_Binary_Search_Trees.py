# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.all_elements = []
        elements_1 = self.traverse(root1, [])
        elements_2 = self.traverse(root2, [])
        # print 'elements_1:', elements_1
        # print 'elements_2:', elements_2
        if len(elements_1) == 0:
            return elements_2
        if len(elements_2) == 0:
            return elements_1
        i = 0
        j = 0
        while i < len(elements_1) or j < len(elements_2):
            if j == len(elements_2) or (i < len(elements_1) and elements_1[i] <= elements_2[j]):
                self.all_elements.append(elements_1[i])
                i += 1
            elif i == len(elements_1) or (j < len(elements_2) and elements_2[j] <= elements_1[i]):
                self.all_elements.append(elements_2[j])
                j += 1
        return self.all_elements

    def traverse(self, node, elements):
        if node is None:
            return elements
        if node.left is not None:
            elements = self.traverse(node.left, []) + elements
        elements.append(node.val)
        if node.right is not None:
            elements += self.traverse(node.right, [])
        return elements

def test_solution(l0, l1):
    test = Solution()
    tree0 = bt.BinaryTree(l0)
    tree1 = bt.BinaryTree(l1)
    # print 'tree0 =', tree0.tolist()
    # print 'tree1 =', tree1.tolist()
    print test.getAllElements(tree0.root, tree1.root)

test_solution([2,1,4], [1,0,3]) # [0,1,1,2,3,4]
test_solution([0,-10,10], [5,1,7,0,2]) # [-10,0,0,1,2,5,7,10]
test_solution([], [5,1,7,0,2]) # [0,1,2,5,7]
test_solution([0,-10,10], []) # [-10,0,10]
test_solution([1,None,8], [8,1]) # [1, 1, 8, 8]