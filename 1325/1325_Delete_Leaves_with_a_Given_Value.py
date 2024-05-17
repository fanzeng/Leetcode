# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        self.target = target
        self.remove(root, None, False)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
        
    def remove(self, n, parent, is_left):
        if n.left is not None:
            self.remove(n.left, n, True)

        if n.right is not None:
            self.remove(n.right, n, False)
        
        if n.left is None and n.right is None and n.val == self.target:
            # print 'val ', n.val, 'is leaf'
            if parent == None: # the node is root
                pass
            else:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
