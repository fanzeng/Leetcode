"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import util.BinaryTree as bt

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.d_level_to_nodes = {}
        self.d_node_to_level = {}
        self.genDicts(root, 0)
        self.connectRecursive(root)
        return root

    def genDicts(self, node, level):
        if node is None:
            return
        self.genDicts(node.left, level+1)
        if self.d_level_to_nodes.get(level) is None:
            self.d_level_to_nodes[level] = [node]
        else:
            self.d_level_to_nodes[level].append(node)
        self.d_node_to_level[node] = (level, len(self.d_level_to_nodes[level])-1)
        self.genDicts(node.right, level+1)

    def connectRecursive(self, n):
        if n is None:
            return
        self.populate(n)
        self.connectRecursive(n.left)
        self.connectRecursive(n.right)

    def populate(self, n):
        if n is None:
            return
        level, index = self.d_node_to_level[n]
        if index + 1 < len(self.d_level_to_nodes[level]):
            n.next = self.d_level_to_nodes[level][index+1]

def print_next(n):
    if n is not None:
        next_val = None
        if hasattr(n, 'next'):
            next_val = n.next.val
        print n.val, ':', next_val
        print_next(n.left)
        print_next(n.right)

def test_solution(l):
    test = Solution()
    tree = bt.BinaryTree(l)
    print 'tree =', tree.tolist()
    print_next(test.connect(tree.root))

test_solution([1,2,3,4,5,None,7])
