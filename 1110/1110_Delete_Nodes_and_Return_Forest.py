# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.forest = [root]
        self.doDelete(root, to_delete)
        return self.forest

    def doDelete(self, root, to_delete):
        for n in to_delete:
            new_roots = []
            for root in self.forest:
                if root.val == n:
                    if root.left is not None:
                        new_roots.append(root.left)
                    if root.right is not None:
                        new_roots.append(root.right)
                    break
                res = self.delete(root, n)
                if len(res) > 0:
                    new_roots = res
                    break
            self.forest = [r for r in self.forest if r.val != n]
            self.forest += new_roots
        
    # deletes n from subtree at root, returns new roots if any
    # else returns []
    # assumes root is not to be deleted
    def delete(self, root, n):
        res = []
        if root is None:
            return res
        if root.left is not None and root.left.val == n:
            if root.left.left is not None:
                res.append(root.left.left)
            if root.left.right is not None:
                res.append(root.left.right)
            root.left = None
        elif root.right is not None and root.right.val == n:
            if root.right.left is not None:
                res.append(root.right.left)
            if root.right.right is not None:
                res.append(root.right.right)
            root.right = None
        else: # neither left or right child is equal to n
            l = self.delete(root.left, n)
            if len(l) > 0:
                return l
            r = self.delete(root.right, n)
            if len(r) > 0:
                return r
        return res
