# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == key:
            if self.isLeaf(root):
                return None
            elif root.left is None:
                return root.right
            else:
                self.remove(root, None, True)
        node, parent = self.search(root.left, root, key)
        if node is None:
            node, parent = self.search(root.right, root, key)
        if node is None:
            return root
        else:
            self.remove(node, parent, node.val < parent.val)
        return root

    def search(self, node, parent, key):
        if node is None:
            return None, None
        if node.val == key:
            return node, parent
        elif node.val < key:
            return self.search(node.right, node, key)
        else:
            return self.search(node.left, node, key)

    def remove(self, node, parent, is_left_child):
        if self.isLeaf(node):
            if is_left_child:
                parent.left = None
            else:
                parent.right = None
            return
        if node.left is None:
            if is_left_child:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            maxNodeInLeft, maxNodeInLeftParent = self.findMax(node.left, node)
            is_left_child = maxNodeInLeft.val < maxNodeInLeftParent.val
            self.swapVal(node, maxNodeInLeft)
            self.remove(maxNodeInLeft, maxNodeInLeftParent, is_left_child)

    def isLeaf(self, node):
        return node.left is None and node.right is None

    def findMax(self, node, parent):
        if node.right is None:
            return node, parent
        else:
            return self.findMax(node.right, node)

    def swapVal(self, a, b):
        temp = a.val
        a.val = b.val
        b.val = temp