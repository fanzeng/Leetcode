# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        d_p = {} # from parent to children
        d_c = {} # from child to parent
        for desc in descriptions:
            p, c, l = desc
            if d_p.get(p) is not None:
                d_p[p][1-l] = c
            else:
                d_p[p] = [None, None]
                d_p[p][1-l] = c
            d_c[c] = p
        # print d_p, d_c
        root = self.find_root(d_p, d_c)
        # print root
        return self.create(root, d_p)

    def find_root(self, d_p, d_c):
        for p in d_p.keys():
            if d_c.get(p) is None:
                return p

    def create(self, p, d_p):
        if p is None:
            return
        n = TreeNode(p)
        if d_p.get(p):
            cl, cr = d_p.get(p)
            n.left = self.create(cl, d_p)
            n.right = self.create(cr, d_p)
        return n
