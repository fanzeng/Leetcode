# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import util.BinaryTree as bt

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        l = self.tolist(root)
        log = 0
        while True:
            log += 1
            if 2**log > len(l):
                break
        complete_len = 2**(log)-1
        print complete_len, len(l)
        for x in xrange(complete_len-len(l)):
            l.append(None)
        print l
        d = 0
        i = 0
        while i + 2**d <= len(l):
            level = l[i:i + 2**d]
            if not self.isListSymmetric(level):
                return False
            i = i + 2**d
            d += 1
        return True


    def isListSymmetric(self, l):
        i = 0
        j = len(l)-1
        while i <= j:
            if l[i] != l[j] and not (l[i] is None and l[j] is None):
                return False
            i += 1
            j -= 1
        return True

    def tolist(self, root):
        l = []
        q = [root]
        while len(q) > 0 and self.is_not_last(q):
            n = q.pop(0)
            if n is None:
                l.append(None)
                q.append(None)
                q.append(None)
            else:
                l.append(n.val)
                q.append(n.left)
                q.append(n.right)
            print self.is_not_last(q)
        return l

    def is_not_last(self, l):
        print len(l)
        for n in l:
            if n is not None:
                return True
        return False

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print test.isSymmetric(tree.root)
test_solution([1, 2, 2, 3, 4, 4, 3])
test_solution([])
test_solution([1])
test_solution([1, 2])
test_solution([1, 2, 2, 1])
test_solution([1, 2, None, 2, 1])
test_solution([1, 2, 2, 2, None, 2])
test_solution([1, 2, 2, None, 3, 3, None])
test_solution([1, 2, 2, None, 3, 3])
test_solution([3, 4, 4, 5, None, None, 5, 6,None, None, 6])
test_solution([2,3,3,4,None,None,4,None,5,5,None,None,6,6,None,7,8,8,7,9,0,0,1,1,0,0,9])
# test_solution([9,14,14,74,None,None,74,None,12,12,None,63,None,None,63,-8,None,None,-8,-53,None,None,-53,None,-96,-96,None,-65,None,None,-65,98,None,None,98,50,None,None,50,None,91,91,None,41,-30,-30,41,None,86,None,-36,-36,None,86,None,-78,None,9,None,None,9,None,-78,47,None,48,-79,-79,48,None,47,-100,-86,None,47,None,67,67,None,47,None,-86,-100,-28,11,None,56,None,30,None,64,64,None,30,None,56,None,11,-28,43,54,None,-50,44,-58,63,None,None,-43,-43,None,None,63,-58,44,-50,None,54,43])
# Given
# a
# binary
# tree, check
# whether
# it is a
# mirror
# of
# itself(ie, symmetric
# around
# its
# center).
#
# For
# example, this
# binary
# tree[1, 2, 2, 3, 4, 4, 3] is symmetric:
#
# 1
# / \
#     2
# 2
# /  \ / \
#     3
# 4
# 4
# 3
#
# But
# the
# following[1, 2, 2, null, 3, null, 3] is not:
#
# 1
# / \
#     2
# 2
# \ \
#     3
# 3
#
# Note:
# Bonus
# points if you
# could
# solve
# it
# both
# recursively and iteratively.