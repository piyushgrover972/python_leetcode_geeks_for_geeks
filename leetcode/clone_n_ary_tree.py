"""
    https://leetcode.com/problems/clone-n-ary-tree/

    Tags: POTD; Trees;
"""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> Optional['Node']:

        if root is None:
            return None

        node = Node(root.val, None)

        for child in root.children:
            node.children.append(self.cloneTree(child))

        # print(f"{id(root):x}->{root.val}, {id(node):x}->{node.val}")
        return node
