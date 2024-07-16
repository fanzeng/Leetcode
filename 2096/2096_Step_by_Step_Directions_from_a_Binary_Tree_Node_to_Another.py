# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        s = startValue
        d = destValue
        path_s, _ = self.path_from_node(root, s, [])
        path_d, direc = self.path_from_node(root, d, [])
        # print path_s
        # print path_d, direc
        
        # reverse the list to get from root to node
        path_s.reverse()
        path_d.reverse()
        direc = direc[::-1]
        index, lca = self.lowest_common_ancestor(path_s, path_d)
        # print index, lca
        return 'U' * (len(path_s) - index - 1) + direc[index:]

    def lowest_common_ancestor(self, path_s, path_d):
        i = 0
        while path_s[i] != path_d[i]:
            i += 1
            if i == len(path_s):
                return -1, None
        while i+1 < len(path_s) and i+1 < len(path_d) and path_s[i+1] == path_d[i+1]:
            i += 1
        return i, path_s[i]

    # Returns a tuple (path, dir)
    # path is the path from node to root
    # dirc is the direction from node to root 
    def path_from_node(self, n, t, p):
        if n is None:
            return None, None
        if n.val == t:
            p.append(n.val)
            return p, '' 
        else:
            l, pl = self.path_from_node(n.left, t, p)
            if l is not None:
                p.append(n.val)
                return p, pl + 'L'
            r, pr = self.path_from_node(n.right, t, p)
            if r is not None:
                p.append(n.val)
                return p, pr + 'R'
            return None, None
