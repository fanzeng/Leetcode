# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import util.BinaryTree as bt

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.l_parent_p = []
        self.l_parent_q = []
        self.isParentOf(root, p.val, self.l_parent_p, 0)
        self.isParentOf(root, q.val, self.l_parent_q, 0)
        common_parents = [x for x in self.l_parent_p if x[0].val in [y[0].val for y in self.l_parent_q]]
        return sorted(common_parents, key=lambda t:-t[1])[0][0]

    def isParentOf(self, n, p, l, d):
        if n is None:
            return False
        if n.val == p or self.isParentOf(n.left, p, l, d+1) or self.isParentOf(n.right, p, l, d+1):
            l.append((n, d))
            return True
        else:
            return False

def test_solution(l, p, q):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.lowestCommonAncestor(tree.root, p, q).val

test_solution([6,2,8,0,4,7,9,None,None,3,5], TreeNode(2), TreeNode(8)) # 6
test_solution([6,2,8,0,4,7,9,None,None,3,5], TreeNode(2), TreeNode(4)) # 2