# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		if p is None:
			if q is None:
				return True
			else:
				return False
		if q is None:
			return False
		if p.left is None:
			if q.left is not None:
				return False
		if p.right is None:
			if q.right is not None:
				return False
		if p.left is None and p.right is None:
			if p.val == q.val:
				return True
			else:
				return False

		return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)