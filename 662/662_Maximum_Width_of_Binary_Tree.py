# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.leftmost = {}
        self.rightmost = {}
        self.treeHeight = 0
        root.label = 0
        self.labelTree(root, 0)
        # print 'self.treeHeight =', self.treeHeight
        self.width = 1 if root is not None else 0
        for h in xrange(self.treeHeight):
            # print h, ':', self.leftmost[h], ',', self.rightmost[h]
            r = self.rightmost[h]
            l = self.leftmost[h]
            if (l < 0 and r < 0) or (l > 0 and r > 0):
                width = r - l + 1
            else:
                width = r - l
            if width > self.width:
                self.width = width
        return self.width

    def labelTree(self, node, depth):
        if depth+1 > self.treeHeight:
            self.treeHeight = depth+1
        if node is not None:
            if self.leftmost.get(depth) is None or node.label < self.leftmost[depth]:
                self.leftmost[depth] = node.label
            if self.rightmost.get(depth) is None or node.label > self.rightmost[depth]:
                self.rightmost[depth] = node.label
        else:
            return
        # print depth, node.val
        if node.left is not None:
            if depth == 0:
                node.left.label = -1
            elif node.label < 0:
                node.left.label = node.label*2
            else:
                node.left.label = node.label*2-1
            self.labelTree(node.left, depth+1)
        if node.right is not None:
            if depth == 0:
                node.right.label = 1
            elif node.label < 0:
                node.right.label = node.label*2+1
            else:
                node.right.label = node.label*2
            self.labelTree(node.right, depth+1)