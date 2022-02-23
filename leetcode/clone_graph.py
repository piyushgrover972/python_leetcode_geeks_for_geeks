"""
    https://leetcode.com/problems/clone-graph/

    Tags: Practice; Concepts; Algorithms; BFS/DFS; Medium
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.nodes = []

    def cloneGraph(self, node: 'Node') -> Optional['Node']:

        if node is None:
            return None

        # Pass 1: Find all nodes in the graph using DFS
        self.findNodes(node)

        # print(self.nodes)

        # Pass 2: Create a copy of all nodes in the graph
        newnodes = {}
        for n in self.nodes:
            newnodes[n.val] = Node(n.val, None)

        # print(newnodes)

        # Pass 3: Populate the neighbors of each node
        for n in self.nodes:
            neighb = n.neighbors

            for nb in neighb:
                newnodes[n.val].neighbors.append(newnodes[nb.val])

        return newnodes[self.nodes[0].val]

    # DFS
    def findNodes(self, node: 'Node'):

        self.nodes.append(node)

        for n in node.neighbors:
            if n not in self.nodes:
                self.findNodes(n)
