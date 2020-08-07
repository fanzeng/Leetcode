# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.d = {}
        self.assignCoordinate(root, 0, 0)
        # print self.d
        res = []
        for key in sorted(self.d.keys()):
            res.append([val[0] for val in sorted(self.d[key], key=lambda x: (-x[1], x[0]))])
        return res


    def assignCoordinate(self, node, x, y):
        if node is None:
            return
        node.coord = (x, y)
        # print node.val, node.coord
        d_res = self.d.get(x)
        if d_res is None:
            self.d[x] = [(node.val, y)]
        else:
            self.d[x].append((node.val, y))
        self.assignCoordinate(node.left, x-1, y-1)
        self.assignCoordinate(node.right, x+1, y-1)

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.verticalTraversal(tree.root)

test_solution([3,9,20,None,None,15,7]) # [[9],[3,15],[20],[7]]
test_solution([1,2,3,4,5,6,7]) #  [[4],[2],[1,5,6],[3],[7]]