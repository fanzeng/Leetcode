# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import util.BinaryTree as bt

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.d_parent = {}
        li = self.traverse(root, None, True)
        # print 'traverse =', [n.val for n in li]
        small = -1
        big = -1
        for i in xrange(len(li)):
            if small == -1 and li[i].val > li[i+1].val:
                small = i
                continue
            if i-1 != small and li[i].val < li[i-1].val:
                big = i
                break
        if big == -1:
            big = small + 1
        # print 'small, big =', small, big
        # print 'swapping', li[small].val, 'with', li[big].val

        # the problem does not require swapping the reference
        # and we need to swap the value instead
        temp = li[big].val
        li[big].val = li[small].val
        li[small].val = temp
        return root

        # the following codes performs the swap when swapping references is required
        # if li[small].val == root.val:
        #     root = self.swapRootWith(root, li[big])
        # elif li[big].val == root.val:
        #     root = self.swapRootWith(root, li[small])
        # else:
        #     self.swapNonRoot(li[small], li[big])
        # return root

    # traverse from node n, record its parent and whether n is the left child of the parent
    def traverse(self, n, parent, is_left):
        if n is None:
            return []
        self.d_parent[n.val] = parent, is_left
        return self.traverse(n.left, n, True) + [n] + self.traverse(n.right, n, False)

    # swap root with a non-root node
    # being non-root, a has a parent
    # returns the new root
    def swapRootWith(self, root, a):
        parent_a, is_left = self.d_parent[a.val]
        if parent_a == root:
            a_left_child = a.left
            a_right_child = a.right
            new_root = a
            if is_left:
                new_root.left = root
                new_root.right = root.right
            else:
                new_root.right = root
                new_root.left = root.left
            root.left = a_left_child
            root.right = a_right_child
        else:
            a_left_child = a.left
            a_right_child = a.right
            a.left = root.left
            a.right = root.right
            root.left = a_left_child
            root.right = a_right_child
            new_root = a
            if is_left:
                parent_a.left = root
            else:
                parent_a.right = root
        return new_root

    # swap two non-root nodes
    # being non-root a and b both have a parent
    def swapNonRoot(self, a, b):
        parent_a, is_left_a = self.d_parent[a.val]
        parent_b, is_left_b = self.d_parent[b.val]

        if parent_a == b:
            a_left_child = a.left
            a_right_child = a.right
            if is_left_a:
                a.left = b
                a.right = b.right
            else:
                a.right = b
                a.left = b.left
            b.left = a_left_child
            b.right = a_right_child
            self.assignChild(parent_b, a, is_left_b)

        if parent_b == a:
            b_left_child = b.left
            b_right_child = b.right
            if is_left_b:
                b.left = a
                b.right = a.right
            else:
                b.right = a
                b.left = a.left
            a.left = b_left_child
            a.right = b_right_child
            self.assignChild(parent_a, b, is_left_a)

        # neither is the parent of the other
        a_left_child = a.left
        a_right_child = a.right
        a.left = b.left
        a.right = b.right
        b.left = a_left_child
        b.right = a_right_child
        self.assignChild(parent_a, b, is_left_a)
        self.assignChild(parent_a, b, is_left_a)

    def assignChild(self, parent, new_child, is_left):
        if is_left:
            parent.left = new_child
        else:
            parent.right = new_child


def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print bt.BinaryTree(test.recoverTree(tree.root)).tolist()

test_solution([1,3,None,None,2])
test_solution([3,1,4,None,None,2])
test_solution([1,2,3])


