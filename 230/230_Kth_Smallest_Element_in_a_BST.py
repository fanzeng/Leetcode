# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.sizeOfDescendants(root)
        root.rank = root.size_of_left_descendants + 1
        self.assignRank(root)
        return self.getkthSmallest(root, k)

    def sizeOfDescendants(self, root):
        if root is None:
            return 0
        size_of_descendants = 0
        size_of_left_descendants = 0
        size_of_right_descendants = 0

        if root.left is not None:
            size_of_left_descendants = 1 + self.sizeOfDescendants(root.left)
            size_of_descendants += size_of_left_descendants
        if root.right is not None:
            size_of_right_descendants = 1 + self.sizeOfDescendants(root.right)
            size_of_descendants += size_of_right_descendants
        root.size_of_left_descendants = size_of_left_descendants
        root.size_of_right_descendants = size_of_right_descendants
        root.size_of_descendants = size_of_descendants
        return root.size_of_descendants

    def assignRank(self, root):
        if root.left is not None:
            root.left.rank = root.rank - 1 - root.left.size_of_right_descendants
            self.assignRank(root.left)

        if root.right is not None:
            root.right.rank = root.rank + 1 + root.right.size_of_left_descendants
            self.assignRank(root.right)

    def getkthSmallest(self, root, k):
        if root is None:
            return None

        if root.rank == k:
            return root.val
        else:
            res_left = self.getkthSmallest(root.left, k)
            if res_left is not None:
                return res_left
            else:
                res_right = self.getkthSmallest(root.right, k)
                if res_right is not None:
                    return res_right


def test_solution(l, k):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.kthSmallest(tree.root, k)

test_solution([3,1,4,None,2], 1) # 1
test_solution([5,3,6,2,4,None,None,1], 3) # 3
test_solution([5,3,6,2,4,None,None,1], 4) # 4
test_solution([1,None,2], 2) # 2