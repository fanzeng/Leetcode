# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.d_val = {}
        self.d_count = {}
        self.addNodeVal(root, 0)
        return [v*1./self.d_count[k] for k, v in self.d_val.items()]

    def addNodeVal(self, node, depth):
        if node is None:
            return
        if self.d_val.get(depth) is None:
            self.d_val[depth] = node.val
        else:
            self.d_val[depth] += node.val
        if self.d_count.get(depth) is None:
            self.d_count[depth] = 1
        else:
            self.d_count[depth] += 1
        self.addNodeVal(node.left, depth+1)
        self.addNodeVal(node.right, depth+1)