class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    '''
        convert list to tree
        list format:
        [ elem_0, elem_1, elem_2, ... ]
        tree:
                  elem_0
                /       \
            elem_1      elem_2
            /   \       /   \
        elem_3 elem_4 elem_5 elem6
                    ...
    '''
    def __init__(self, l):
        if l is None or len(l) == 0:
            self.root = None
        else:
            self.root = TreeNode(l[0])
            leafs = [self.root]
            self.depth = 1
            i = 1
            while i < len(l):
                new_leafs = []
                for leaf in leafs:
                    leaf.left = TreeNode(l[i])
                    if leaf.left.val is not None:
                        new_leafs.append(leaf.left)
                    i += 1
                    if i == len(l):
                        break
                    leaf.right = TreeNode(l[i])
                    if leaf.right.val is not None:
                        new_leafs.append(leaf.right)
                    i += 1
                    if i == len(l):
                        break
                leafs = new_leafs
                self.depth += 1

    def tolist(self):
        l = []
        if self.root is None:
            return l
        n = self.root
        q = [n]
        while len(q) > 0:
            n = q.pop(0)
            if n is None:
                l.append(None)
            else:
                l.append(n.val)
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
        last_leaf = len(l)-1
        while l[last_leaf] is None:
            last_leaf -= 1
        return l[:last_leaf+1]

if __name__ == '__main__':
    bt = BinaryTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print 'bt.tolist()', bt.tolist()
    bt = BinaryTree([0, 1, 2, 3, 4, None, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    print 'bt.tolist()', bt.tolist()
    bt = BinaryTree([3, 4, 4, 5, None, None, 5, 6,None, None, 6])
    print 'bt.tolist()', bt.tolist()
