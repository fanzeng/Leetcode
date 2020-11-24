# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = {} # node: (max rob result of sub-tree rooted at node, max rob result of sub-tree rooted at node if node itself is not robbed)
        return self.robDP(root)[0]

    def robDP(self, node):
        if node is None:
            return (0, 0)
        if self.d.get(node) is not None:
            return self.d[node]
        res_left = self.robDP(node.left)
        res_right = self.robDP(node.right)
        res_rob_node = node.val + res_left[1] + res_right[1]
        res_not_rob_node = res_left[0] + res_right[0]
        res = (max(res_rob_node, res_not_rob_node), res_not_rob_node)
        self.d[node] = (res_rob_node, res_not_rob_node)
        return res

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.rob(tree.root)

test_solution([3,2,3,None,3,None,1]) # 7
test_solution([3,4,5,1,3,None,1] ) # 9
test_solution([] ) # 9