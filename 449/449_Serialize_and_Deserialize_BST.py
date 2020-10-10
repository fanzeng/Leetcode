# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import util.BinaryTree as bt
from util.BinaryTree import TreeNode

# note: this current version does not make full use of the BST, in fact, it works with any binary tree

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.serializeNode(root, '')

    def serializeNode(self, node, s):
        if node is None:
            return ''
        s_left = '()'
        if node.left is not None:
            s_left = self.serialize(node.left)
        s_right = '()'
        if node.right is not None:
            s_right = self.serialize(node.right)
        return '(' + str(node.val) + s_left + s_right + ')'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.deserializeNode(data)

    def deserializeNode(self, data):
        # print 'data=', data
        if data is None or len(data) == 0:
            return None
        assert(data[0] == '(' and data[-1] ==')')
        if data == '()':
            return None
        data = data[1:-1]
        paren_start_l = data.find('(')
        node = TreeNode(int(data[:paren_start_l]))
        paren_span = self.findParenEnd(data[paren_start_l:])
        paren_end_l = paren_start_l + paren_span
        node.left = self.deserializeNode(data[paren_start_l:paren_end_l+1])

        paren_start_r = paren_end_l + 1
        paren_span = self.findParenEnd(data[paren_start_r:])
        paren_end_r = paren_start_r + paren_span
        node.right = self.deserializeNode(data[paren_start_r:paren_end_r+1])
        return node

    def findParenEnd(self, s):
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append('(')
            if c == ')':
                stack.pop()
            if len(stack) == 0:
                return i

def test(l):
    ser = Codec()
    deser = Codec()
    tree = ser.serialize(bt.BinaryTree(l).root)
    print 'serialized =', tree
    ans = deser.deserialize(tree)
    if ans is None:
        return None
    else:
        print bt.BinaryTree(ans).tolist()

test([2,1,3]) # [2,1,3]
test([]) # []
test([5,3,7,1,4,6,9,0,2,None,None,None,None,8,10]) # [5,3,7,1,4,6,9,0,2,None,None,None,None,8,10]