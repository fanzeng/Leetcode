# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        return self.isValidSequenceRecursive(root, arr)

    def isValidSequenceRecursive(self, root, arr):
        if root is None:
            if arr is None or len(arr) == 0:
                return True
            else:
                return False
        if root.val != arr[0]:
            return False
        if len(arr) == 1:
            return root.left is None and root.right is None
        else:
            return self.isValidSequenceRecursive(root.left, arr[1:]) or self.isValidSequenceRecursive(root.right, arr[1:])

test = Solution()
print test.isValidSequence(bt.BinaryTree([0,1,0,0,1,0,None,None,1,0,0]).root, [0,1,0,1])
print test.isValidSequence(bt.BinaryTree([0,1,0,0,1,0,None,None,1,0,0]).root, [0,0,1])
print test.isValidSequence(bt.BinaryTree([0,1,0,0,1,0,None,None,1,0,0]).root, [0,1,1])
print test.isValidSequence(bt.BinaryTree([8,3,None,2,1,5,4]).root, [8])