# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import util.BinaryTree as bt

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        if root is None:
            return self.res
        else:
            self.zigzag(root, 0)
            for i, r in enumerate(self.res):
                if i % 2 == 1:
                    self.res[i] = r[::-1]
            return self.res

    def zigzag(self, node, depth):
        if node is None:
            return
        if not depth < len(self.res):
            self.res.append([])
        self.res[depth].append(node.val)
        if node.left is None and node.right is None:
            return
        self.zigzag(node.left, depth+1)
        self.zigzag(node.right, depth+1)

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.zigzagLevelOrder(tree.root)

test_solution([3,9,20,None,None,15,7]) # [[3], [20,9], [15,7]]
test_solution([1,2,3,4,None,None,5]) # [[1],[3,2],[4,5]]

