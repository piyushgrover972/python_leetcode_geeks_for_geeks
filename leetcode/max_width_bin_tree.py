"""
    https://leetcode.com/problems/maximum-width-of-binary-tree/

    Tags: POTD; Medium; Binary Tree; BFS/Level Order
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.nodes = {}
        self.width = {}

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        self.bfs([(root, 1, 1)])

        # print(self.nodes)

        for lvl, nodes in self.nodes.items():
            self.width[lvl] = nodes[-1] - nodes[0] + 1

        return max(self.width.values())

    def bfs(self, q: List):

        if q:
            node, lvl, val = q.pop(0)

            if node is not None:
                # print(node.val)

                if lvl in self.nodes:
                    self.nodes[lvl].append(val)
                else:
                    self.nodes[lvl] = [val]

                q.append((node.left, lvl + 1, val * 2))
                q.append((node.right, lvl + 1, (val * 2) + 1))

            self.bfs(q)
