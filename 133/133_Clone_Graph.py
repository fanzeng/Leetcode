"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        if node == []:
            return []
        if node == [[]]:
            return [[]]
        self.d = {}
        return self.cloneNode(node)


    def cloneNode(self, node):
        if self.d.get(node.val) is not None:
            return self.d[node.val]
        new_node = Node(node.val)
        self.d[node.val] = new_node
        new_neighbors = []
        for neighbor in node.neighbors:
            new_neighbors.append(self.cloneNode(neighbor))
        self.d[node.val].neighbors = new_neighbors
        return new_node