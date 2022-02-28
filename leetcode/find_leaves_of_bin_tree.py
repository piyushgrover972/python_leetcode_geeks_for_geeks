"""
    https://leetcode.com/problems/find-leaves-of-binary-tree/

    Tags: Google; Medium; Binary Tree; Traversal
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.nodes = {}

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.traverse(root)

        return list(self.nodes.values())

    def traverse(self, node: Optional[TreeNode]):

        if node is not None:

            idx_l = self.traverse(node.left)
            idx_r = self.traverse(node.right)

            lvl = max(idx_l, idx_r)

            if lvl in self.nodes:
                self.nodes[lvl].append(node.val)
            else:
                self.nodes[lvl] = [node.val]

            return lvl + 1

        else:
            return 0
